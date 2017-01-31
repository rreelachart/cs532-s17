#!/usr/local/bin/python3

import sys
import re
import urllib2
from urllib2 import urlopen
from urllib2 import HTTPError
import httplib2

URIPATTERN = re.compile(r'(?:http://[\S]*|https://[\S]*)')

#Gets the URI from given string
def extractURI(line):
	return URIPATTERN.findall(line)
	
#Gets the URI after redirects and ending in a 200 code
def extractFinalURI(uri):
	FinalURI = None
	
	try:
		request = urlopen(httplib2.iri2uri(uri))
		if request.getcode() == 200:
			FinalURI = request.geturl()
	except urllib2.HTTPError as e:
		FinalURI = None
	except urllib2.URLError as e:
		FinalURI = None
	except UnicodeError as e:
		FinalURI = None
		
	return FinalURI
	
if __name__ == "__main__":
	filenames = sys.argv[1:]
	for filename in filenames:
		f = open(filename)
		
		for line in f:
			sys.stderr.write("Working on: " + line + '\n')
			URIs = extractURI(line)
			
			for URI in URIs:
				sys.stderr.write("Trying URI: [" + URI + ']\n')
				goodURI = extractFinalURI(URI)
				
				if goodURI:
					print(goodURI)
		
		f.close()