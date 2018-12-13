import GitHack
import testsvn
import newdbLeakscan
import hgbzr
import ds_store_exp
import main2
class connectinterface():
	def __init__(self,urllist):
		self.s1,self.s2,self.s3,self.s4,self.s5,self.s6,self.s7=[],[],[],[],[],[],[]
		self.tmp=[]
		self.tmp=urllist
		self.u=urllist[0]
		self.t=urllist[1]
		self.time=urllist[2]
			

	def interfaceSet01(self):
		try:
			print "scan type1"
			u1=self.u+"/.git"
			self.s1=GitHack.githack(u1)
		except:
			pass
			return self.s1
	def interfaceSet02(self):
		try:
			print "scan type2"
			u2=self.u+"/.svn/entries"
			self.s2=testsvn.svnTest(u2)
		except:
			pass
			return self.s2

	def interfaceSet03(self):
		try:
			print "scan type3"
			self.s3=newdbLeakscan.dbfinal(tmp)
		except:
			pass
			return self.s3
	def interfaceSet04(self):
		try:
			print "scan type4"
			u5=self.u+"/.bzr/"
			self.s4=hgbzr.usebzr(u5)
		except:
			pass
			return self.s4
	def interfaceSet05(self):
		try:
			print "scan type5"
			u6=self.u+"/.hg/"
			self.s5=hgbzr.usehg(u6)
		except:
			pass
			return self.s5
	def interfaceSet06(self):
		try:
			print "scan type6"
			u4=self.u+"/"
			self.s6=main2.ctfwebscan(u4)
		except:
			pass
			return self.s6	
	def interfaceSet07(self):
		try:
			print "scan type7"
			u3 = self.u+"/.DS_Store"
			self.s7=ds_store_exp.ds_store_exp(u3)
		except:
			pass
			return self.s7
#interfaceSet("https://kubuntu.org")
