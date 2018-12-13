#!coding:utf-8
""" Auther: 加菲猫 """
from optparse import OptionParser 
import urllib
import urlparse
import re
import os
import sys

class Svn_Hack():
    def __init__(self):
        self.root_dir = None
        self.url = None
        self.name = None

    def is_exists(self, Dir):
        if not os.path.exists(Dir):
            return True
        else:
            return False
        
    def Fetch_Dic(self, entries_url):
        res=urllib.urlopen(entries_url).read()
        try:
            dic = re.findall(r'\n(.*?)\ndir',res)
            dic.remove('')
        except Exception:
            dic = []
      
        next_url_list = []
        if len(dic) != 0:
            for i in dic:
                 url = entries_url.split('.svn')[0]+i+'/.svn/entries'
                 path = "./"+self.root_dir+urlparse.urlparse(url).path
                 if self.is_exists(path):
                     os.makedirs(path)

                 next_url_list.append(url)

        return next_url_list


    def DownFile(self, entries_url):
        res=urllib.urlopen(entries_url).read()
        try:
            dic = re.findall(r'\n(.*?)\nfile',res)
        except Exception:
            dic = []

        if len(dic) != 0:
            for i in dic:
                 url=entries_url.split('.svn')[0]+i
                 path = "./"+self.root_dir+urlparse.urlparse(url).path
                 res=urllib.urlopen(url).read()
                 print "[Fetch] %s" % url
                 with open(path,'a+') as f:
                     f.write(res)

    def DownSite(self):
        res=urllib.urlopen(self.url).read()

        self.root_dir = urlparse.urlparse(self.url).netloc

        # 初始化下载目录
        if self.is_exists(self.root_dir):
            os.mkdir(self.root_dir)

        # 获取所有svn目录
        dir_list = []
        dic = re.findall(r'\n(.*?)\ndir',res)

        print len(dic)

        for i in dic:
            # 空目录跳过
            if i == '':
                continue

            # 循环下载所有目录
            if self.is_exists(self.root_dir+"/"+i):
                os.mkdir(self.root_dir+"/"+i)
                entries_url = self.url.split('.svn')[0]+i+'/.svn/entries'
                dir_list.append(entries_url)
                while len(dir_list) != 0:
                    next_dic = self.Fetch_Dic(dir_list.pop())
                    if len(next_dic) != 0:
                        for url in next_dic:
                            dir_list.append(url)
                            self.DownFile(url)
                            #print url, len(dir_list)

            #sys.exit()

        # 下载根目录文件
        self.DownFile(self.url)
     

	#自定义的函数
    def readmingl(self,url):
        if url != None:
            self.url = url
		    #直接将下载整站
            self.DownSite()
        return self.root_dir
               

def svnTest(url):
	svn = Svn_Hack()
	name=svn.readmingl(url)
	s=[]
	a="stored in "+name
 	s.append(a)
	return s
