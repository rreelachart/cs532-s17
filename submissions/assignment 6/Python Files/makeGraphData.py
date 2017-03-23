import commands
import json
import time
	
def passTrueLinksSourceAndTarget():
	read = open('twitterTrueLinks','r')
	data= json.load(read)
	for user in data:
		getIds(user["source"],user["target"])
			
def getIds(name1,name2):
	read = open('twitterNodes','r')
	f2 = open('graphIDs','a')
	data= json.load(read)
	for user in data:
		dict ={}
		if name1 == user["screenName"]:
			id = user["id"]
			dict['source'] = id
			f2.write(json.dumps(dict)+",\n")
		elif name2 == user["screenName"]:
			id = user["id"]
			dict['target'] = id
			f2.write(json.dumps(dict)+",\n")
	f2.close()

passTrueLinksSourceAndTarget()