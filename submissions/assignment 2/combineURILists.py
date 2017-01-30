#!/usr/local/bin/python3

import sys

inputFilenames = sys.argv[1:]

urilist = []

#combine all lists from given files
for filename in inputFilenames:
	f = open(filename)
	urilist.extend(f.readlines())
	f.close()
	
#sort list
urilist.sort()

#find uniques
urilist = list(set(urilist))

#sort again after uniques
urilist.sort()

for entry in urilist:
	print(entry.strip())