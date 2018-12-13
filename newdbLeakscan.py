#! /usr/bin/python
# -*- coding:utf-8 -*-
#author:xq17

import requests
import threading
import re
import sys
import time

lock = threading.Lock()
other_list = []
success_list = []

#多线程类
class myThread(threading.Thread):
	def __init__(self,url,time_out):
		threading.Thread.__init__(self)
		self.url = url
		self.time_out = time_out
	def run(self):
		scan(self.url,self.time_out)

#扫描url
def scan(url,time_out):
	try:
		response = requests.head(url,timeout=time_out)
		code = response.status_code
		lock.acquire()  #输出加锁
		if code == 200:
			success_list.append(str(code)+":"+url)
			#print url +"  200 Resource Found!!!"
		else:
			other_list.append(str(code)+":"+ url)
			#print "Resource Not found"
	except Exception as e:
		lock.acquire()
		print e
	finally:
		lock.release()

#url格式化
def urlFormat(url):
	if (not url.startswith("http://")) and (not url.startswith("https://")):
		url = "http://"+ url
	if not url.endswith("/"):
		url = url + "/"
	return url

#自动生成相关备份
def  bak_auto(website):
	bak_list = []
	normal_suffix = ['.rar','.zip','.7z','.tar.gz','.bak','.swp','.txt','.html',]
	url_cut = re.search('[\.|\/](.*)\..*?$',website).group(1).replace("/www.","").replace("/","").replace(".","")
	for i in normal_suffix:
		bak_list.append(url_cut+i)
		bak_list.append(url_cut+'db'+i)
		bak_list.append(url_cut+'_db'+i)
	return bak_list
#优质字典
def dict_fuzz(website):
	dict_1 = ['wwwroot.rar','wwwroot.zip','wwwroot.tar','wwwroot.tar.gz','web.rar','web.zip','web.tar.gz',
	'ftp.rar','frp.rar.gz','ftp.zip','data.rar','data.zip','data.tar.gz','data.tar','admin.rar','admin.zip',
	'admin.tar','admin.tar.gz','www.zip','www.tar','www.tar.gz','flashfxp.rar','flashfxp.zip','flashfxp.tar',
	'flashfxp.tar.gz','#domain#.rar','#domain#.zip','#domain#.tar','#domain#.tar.gz','#underlinedomain#.tar',
	'#domainnopoint#.tar', '#topdomain#.tar', '#domaincenter#.tar', '#underlinedomain#.tar.gz', '#domainnopoint#.tar.gz',
	'#topdomain#.tar.gz', '#domaincenter#.tar.gz', '#underlinedomain#.zip', '#domainnopoint#.zip', '#topdomain#.zip', 
	'#domaincenter#.zip', '#underlinedomain#.rar', '#domainnopoint#.rar', '#topdomain#.rar', '#domaincenter#.rar', 
	'#underlinedomain#.7z', '#domainnopoint#.7z', '#topdomain#.7z', '#domaincenter#.7z']
	return dict_1

#ctf字典
def ctf_fuzz(website):
	dict_2 = ['help.php','file.txt','file.php','help.txt','flag.php','flag.txt','fl4g.php','fl4g.txt','flAg.php','flAg.txt',
	'index.php~','index.un~','index.swp','index.~','index.bak','index.bak.php','.bash_history','index.php.swm','phpinfo.php','.svn',
	'index-bak','info.php','test.php','.?.swp','.git','?.bak']
	return dict_2

#主程序
def test(u):
	argvlist=[0,0,0]
	argvlist[0]=u
	argvlist[1]=2
	argvlist[2]=2
	#print argvlist
	testmain(argvlist)
	
def success_list_w():
	fp = open("successres.txt",'w+')
	for url in success_list:
		fp.write(url+'\n')
	fp.close()	
	
def testmain(argvlist):
	if argvlist[0]==0:
	#没有输入url，直接退出
		'''print " Usage:"
		print "    python dbLeakscan.py [url] [thread_number] [time_out]"
		print " Example:"
		print "    python dbLeakscan.py http://localhost/ 5 2"
		print " Author:"
		print "    xq17 from mst society"
		exit(1)'''
		exit(1)
	if argvlist[1]==0:
	#输入url，但是线程数没有设置
		argvlist[1]=1
		#print "默认线程数"
	if argvlist[2]==0:
	#输入url，但是没有设置超时
		argvlist[2]=2
		#print "默认超时时间"
	website = urlFormat(argvlist[0])
	thread_number = int(argvlist[1])
	time_out = float(argvlist[2]) 
	if time_out <= 0:
		time_out = 1
	bak_list = bak_auto(website) + dict_fuzz(website) + ctf_fuzz(website)
	threads = []
	for k in bak_list:
		url = website + k
		t = myThread(url,time_out)
		threads.append(t)
	for thread in threads:
		thread.setDaemon(True)
		thread.start()
		while True:
			if (threading.activeCount() < thread_number):
				break
	thread.join()
	
def dbfinal(argvlist):
	testmain(argvlist)
	success_list_w()
	a="stored in ./successres.txt"
 	s=[]
	s.append(a)
	return s


