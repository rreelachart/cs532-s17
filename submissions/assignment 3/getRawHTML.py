#!/usr/local/bin/python2.7

import sys
import re
import urllib2

def extractHTML(uri):
	response = urllib2.urlopen(uri)
	html = response.read()
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
		f.write(rawHTML)
		f.close()
		
	f.close()