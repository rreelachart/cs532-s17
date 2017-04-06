#!/usr/bin/python2.7

import json

def getMaleUsersWithAge():
	f = open('maleUsers','r')
	userData = json.load(f)
	f1 = open('maleUsersWithAge','w')
	ageCount = 0
	maleCount = 0
	for user in userData:
		maleCount += 1
		if user['user_details']['age'] == '27':
			ageCount += 1
			f1.write(json.dumps(user) + ',\n')
	print "Number of male users:" +str(maleCount)
	print "Number of male users who are age 27:" +str(ageCount)

getMaleUsersWithAge()