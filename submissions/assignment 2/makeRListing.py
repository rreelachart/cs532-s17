#!/usr/local/bin/python2.7

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

mementoFile = sys.argv[1]
ageFile = sys.argv[2]

mementoList = {}
ageList = {}

f = open(mementoFile)

for line in f:
	line = line.strip()
	(mementoCount, uri) = line.split('\t')
	
	if int(mementoCount) > 0:
		mementoList[uri] = mementoCount
		
f.close()

f = open(ageFile)

for line in f:
	line = line.strip()
	(age, uri) = line.split('\t')
	
	ageList[uri] = age
	
f.close()

for key in mementoList:
	print(key + '\t' + mementoList[key] + '\t' + ageList[key])