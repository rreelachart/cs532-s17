#!usr/bin/python2.7

def getAtoms():
	file= open('100BlogUris','r')
	f1= open('atomsFromsBlogs','w')
	add= "feeds/posts/default?max-results=1000"
	for uri in file:
		uri= uri.strip()+add 
		f1.write(uri+"\n")
		
getAtoms()