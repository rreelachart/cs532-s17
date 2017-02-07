#!/usr/local/bin/python2.7

import sys
import time
import datetime

reload(sys)
sys.setdefaultencoding('utf-8')

datelistfile = sys.argv[1]

f = open(datelistfile)

for line in f:
	try:
		line = line.strip()
		(final, cdate, uri) = line.split('\t')
		ctime = time.strptime(cdate, "%Y-%m-%dT%H:%M:%S")
		cdtime = datetime.datetime.fromtimestamp(time.mktime(ctime))
		now = datetime.datetime.now()
		days = (now - cdtime).days
		print(str(days) + '\t' + uri)
	except ValueError:
		#pass
		print(str(0) + '\t' + uri)

f.close()