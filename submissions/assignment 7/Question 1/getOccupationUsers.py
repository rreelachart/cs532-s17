#!/usr/bin/python2.7

import json

def getMaleUsersWithAgeAndOccup():
	f = open('maleUsersWithAge','r')
	userData = json.load(f)
	f1 = open('maleUsersWithAgeAndOccup','w')
	ageCount = 0
	occupCount = 0
	for user in userData:
		ageCount += 1
		if user['user_details']['occupation']=='student':
			occupCount+= 1
			f1.write(json.dumps(user) + ',\n')
	print "Number of male users who are age 27:" +str(ageCount)
	print "Number of male users who are age 27 and a Student:" +str(occupCount)
	
getMaleUsersWithAgeAndOccup()