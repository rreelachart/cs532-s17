#!/usr/local/bin/python2.7

import re
import sys
import urllib2
from urllib2 import urlopen
from urllib2 import HTTPError
import httplib2

datePATTERN = re.compile(r'("[^"]*Final:[^"]*")')
	
def findDates(date_line):

	line = len(datePATTERN.findall(str(date_line)))
		
	return line
	
if __name__=="__main__":
	inputfile = sys.argv[1]
	
	f = open(inputfile)
	
	for line in f:
		#date = findDates(line.strip())	
		#print(str(date))
		#sys.stdout.flush()
		if "Final:" in line:
			print(line)
	f.close()