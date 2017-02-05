#!/usr/local/bin/python2.7

import re
import sys
import urllib2
from urllib2 import urlopen
from urllib2 import HTTPError
import httplib2

MementoPATTERN = re.compile(r'(rel="[^"]*memento[^"]*")')

def getTimeMap(uri):
	urit = "http://memgator.cs.odu.edu/timemap/link/" + uri
	
	try:
		request = urlopen(urit)
		
		if request.getcode() == 200:
			#Thanks to the question at 'widequestion.com/question/decode-utf-8-in-python-2-7/' for helping with the next line
			timemap = urllib2.urlopen(urit).read()
			request.close()
		else:
			timemap = None
			request.close()
			
	except urllib2.HTTPError as e:
		timemap = None
		
	except urllib2.URLError as e:
		timemap = None
		
	return timemap
	
def countMementos(uri):
	urit = getTimeMap(uri)
	
	if not urit:
		count = 0
	else:
		count = len(MementoPATTERN.findall(str(urit)))
		
	return count
	
if __name__=="__main__":
	inputfile = sys.argv[1]
	
	f =  open(inputfile)
	
	for uri in f:
		mementoCount = countMementos(uri.strip())
		
		print(str(mementoCount) + "\t" + uri.strip())
		sys.stdout.flush()
	f.close()