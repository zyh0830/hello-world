import os
def usebzr(url):
	hp=url
	os.system("chmod +x rip-bzr.pl") 
	os.system("./rip-bzr.pl -v -u "+hp)
	s=[]
	a="stored in ./bzr"
	s.append(a)
	return s

def usehg(url):
	hp=url
	os.system("chmod +x rip-hg.pl") 
	os.system("./rip-hg.pl -v -u "+hp)
	s=[]
	a="stored in ./hg"
	s.append(a)
	return s
