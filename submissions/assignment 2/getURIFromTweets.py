#!/usr/local/bin/python3

import sys
import re
import urllib.request
import httplib2

URIPATTERN = re.compile("http://[\S]*")

#Gets the URI from given string
def extractURI(line):
	return URIPATTERN.findall(line)
	
#Gets the URI after redirects and ending in a 200 code
def extractFinalURI(uri):
	FinalURI = None
	
	try:
		request = urllib.request.urlopen(httplib2.iri2uri(uri))
		if request.getcode() == 200:
			FinalURI = request.geturl()
	except urlib.error.HTTPError as e:
		FinalURI = None
	except urllib.error.URLError as e:
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
			
			for URI in URIS:
				sys.stderr.write("Trying URI: [" + URI + ']\n')
				goodURI = extractFinalURI(URI)
				
				if goodURI:
					print(goodURI)
		
		f.close()