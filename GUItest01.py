#!/usr/bin/env python
# -*- coding: utf-8 -*-
'a hello world GUI example.'

import Tkinter as tk
from Tkinter import *
import tkMessageBox
import re
import requests
import interfaceSet as itf

def scanstart():
	#获取输入框的值
	url=url_text.get()
	thread=thread_text.get()
	timeout=timeout_text.get()
	#print type(url)
	#print type(thread)
	#print type(timeout)

	#判断url是否为空
	if(url==''):
		tkMessageBox.showwarning('警告','URL不能为空')
		thread_text.set('')
		timeout_text.set('')
	#判断URL是否有效
	elif(not re.match(r'^https?:/{2}\w.+$',url)):
		tkMessageBox.showwarning('警告','此URL无效')
		url_text.set('')
		thread_text.set('')
		timeout_text.set('')
	else:
		if(thread=='' or timeout==''):
			thread=0
			timeout=0		
		list1=[]
		list1.append(url)
		list1.append(thread)
		list1.append(timeout)
		print list1
		#判断url能否连接请求资源
		url=list1[0]
		r = requests.get(url, timeout=5)
		code = r.status_code
		if code != 200: 
			tkMessageBox.showwarning('警告','URL连接失败')
			url_text.set('')
			thread_text.set('')
			timeout_text.set('')
		else:
			#扫描网站
			it=itf.connectinterface(list1)
			res_text.insert(tk.END,"scan start...\n")
			#Type1 scan
			res_text.insert(tk.END,"scan Type1 start...\n")
			reslist=[]
			reslist=it.interfaceSet01()
			if reslist==[]:
				res_text.insert(tk.END,"Type1 Not Found...\n")
			else:
				for i in reslist:
					res_text.insert(tk.END,i)
					res_text.insert(tk.END,"\n")
			res_text.insert(tk.END,"scan Type1 end...\n")
			#Type2 scan
			res_text.insert(tk.END,"scan Type2 start...\n")
			reslist=[]
			reslist=it.interfaceSet02()
			if reslist==None:
				res_text.insert(tk.END,"Type2 Not Found...\n")
			else:
				print reslist
				for i in reslist:
					res_text.insert(tk.END,i)
					res_text.insert(tk.END,"\n")
			res_text.insert(tk.END,"scan Type2 end...\n")
			#Type3 scan
			res_text.insert(tk.END,"scan Type3 start...\n")
			reslist=[]
			reslist=it.interfaceSet03()
			if reslist==None:
				res_text.insert(tk.END,"Type3 Not Found...\n")
			else:
				for i in reslist:
					res_text.insert(tk.END,i)
					res_text.insert(tk.END,"\n")
			res_text.insert(tk.END,"scan Type3 end...\n")

			#Type4 scan
			res_text.insert(tk.END,"scan Type4 start...\n")
			reslist=[]
			reslist=it.interfaceSet04()
			if reslist==None:
				res_text.insert(tk.END,"Type4 Not Found...\n")
			else:
				for i in reslist:
					res_text.insert(tk.END,i)
					res_text.insert(tk.END,"\n")
			res_text.insert(tk.END,"scan Type4 end...\n")

			#Type5 scan
			res_text.insert(tk.END,"scan Type5 start...\n")
			reslist=[]
			reslist=it.interfaceSet05()
			if reslist==None:
				res_text.insert(tk.END,"Type5 Not Found...\n")
			else:
				for i in reslist:
					res_text.insert(tk.END,i)
					res_text.insert(tk.END,"\n")
			res_text.insert(tk.END,"scan Type5 end...\n")

			#Type6 scan
			res_text.insert(tk.END,"scan Type6 start...\n")
			reslist=[]
			reslist=it.interfaceSet02()
			if reslist==None:
				res_text.insert(tk.END,"Type6 Not Found...\n")
			else:
				for i in reslist:
					res_text.insert(tk.END,i)
					res_text.insert(tk.END,"\n")
			res_text.insert(tk.END,"scan Type6 end...\n")

			#Type7 scan
			res_text.insert(tk.END,"scan Type7 start...\n")
			reslist=[]
			reslist=it.interfaceSet02()
			if reslist==None:
				res_text.insert(tk.END,"Type7 Not Found...\n")
			else:
				for i in reslist:
					res_text.insert(tk.END,i)
					res_text.insert(tk.END,"\n")
			res_text.insert(tk.END,"scan Type7 end...\n")
			res_text.insert(tk.END,"scan end...\n")
		



window=tk.Tk()
window.title('scan')
#设置窗口大小
width = 800
height = 600
#获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
screenwidth = window.winfo_screenwidth()  
screenheight = window.winfo_screenheight() 
alignstr = '%dx%d+%d+%d' % (width, height,(screenwidth-width)/2, (screenheight-height)/2)   
window.geometry(alignstr)
#设置窗口是否可变长、宽，True：可变，False：不可变
window.resizable(width=False, height=True)


#窗口内容

fm1=tk.Frame(window)
fm2=tk.Frame(window)

url=tk.Label(fm1,text='Input url:',font=('Arial',20),width=15,height=2).grid(row=0,column=0,padx=3,pady=2)
url_text=StringVar()
url_text.set('')
inputurl=tk.Entry(fm1,width = 30,font=('Arial',20),textvariable=url_text).grid(row=0,column=1,padx=3,pady=2)

threads=tk.Label(fm1,text='Input theads:',font=('Arial',20),width=15,height=2).grid(row=1,column=0,padx=3,pady=2)
thread_text=StringVar()
thread_text.set('')
inputthreads=tk.Entry(fm1,width = 30,font=('Arial',20),textvariable=thread_text).grid(row=1,column=1,padx=3,pady=2)

time=tk.Label(fm1,text='Input timeout:',font=('Arial',20),width=15,height=2).grid(row=2,column=0,padx=3,pady=2)
timeout_text=StringVar()
timeout_text.set('')
inputtimeout=tk.Entry(fm1,width = 30,font=('Arial',20),textvariable=timeout_text).grid(row=2,column=1,padx=3,pady=2)

scanbutton=tk.Button(fm1,text='scan',font=('Arial',20),width=15,height=1,command=scanstart).grid(row=3,column=1,padx=3,pady=2)
on_hit=False#按钮默认的初始状态为False


res=tk.Label(fm2,text='Results',font=('Arial',20),width=15,height=2).grid(row=0,column=0,padx=3,pady=1)

res_text=tk.Text(fm2,width=100,height=15,bg="white")
res_text.insert(1.0,"result...\n")
res_text.grid(row=1,column=0,padx=45,pady=1)

fm1.grid(row=0,column=0,padx=5,pady=3)
fm2.grid(row=1,column=0,padx=5,pady=3)

window.mainloop()
