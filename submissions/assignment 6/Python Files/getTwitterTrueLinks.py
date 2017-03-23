import commands
import json
import time

def getTrueLinks():
	read = open('twitterLinksData','r')
	f2 = open('twitterTrueLinks','w')	
	data= json.load(read)
	for user in data:
		dict = {}
		if user["following"] == True:
			dict['source']= user["screen_name1"]
			dict['target']= user["screen_name2"]
			f2.write(json.dumps(dict)+",\n")
		elif user["followed_by"]== True:
			dict['source']= user["screen_name2"]
			dict['target']= user["screen_name1"]
			f2.write(json.dumps(dict)+",\n")

getTrueLinks()