#!/usr/local/bin/python2.7

import sys
import re
import urllib2
from urllib2 import urlopen
from urllib2 import HTTPError
import httplib2

def extractHTML(uri):
	#Similar code to getURIFromTweets.py to avoid 404 errors
	html = None
	
	try:
		request = urlopen(httplib2.iri2uri(uri))
		if request.getcode() == 200:
			html = request.read()
	except urllib2.HTTPError as e:
		html = None
	except urllib2.URLError as e:
		html = None
	except UnicodeError as e:
		html = None
		
	return html

if __name__ == "__main__":
	filename = sys.argv[1]
	f = open(filename)
		
	#Credit to "http://stackoverflow.com/questions/13798447/write-multiple-files-at-a-time" for how to output to seperate files.	
	for i, line in enumerate(f):
		sys.stderr.write("Working on: " + line + '\n')
		f = open("URI_%i.raw" %i, 'w')
		rawHTML = extractHTML(line)
		f.write("RAW HTML FOR: " + line)
		f.write(str(rawHTML))
		f.close()
		
	f.close()