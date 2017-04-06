#!/usr/bin/python2.7

import json

def getMaleUsers():
	f = open('maleUsers','w')
	userDataFile = open("userData.json","r")
	userData = json.load(userDataFile)
	count = 0
	maleCount = 0
	for user in userData:
		count += 1
		if user['user_details']['gender'] =='M':
			maleCount += 1
			f.write(json.dumps(user) + ',\n')
	print "Total users:" +str(count)
	print "Number of male users:" +str(maleCount)

getMaleUsers()