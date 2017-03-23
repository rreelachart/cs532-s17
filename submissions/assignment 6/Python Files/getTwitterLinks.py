import sys
import json
import time

f1 = open('twitterLinks','w')
read = open('twitterNodes','r')
def links():
	userData =[]
	for line in read:
		data= json.loads(line)
		for user in data:
			dict = {}
			dict['source'] = user['id']
			dict['target'] =  0
			userData.append(dict)
	f1.write(json.dumps(userData)+"\n")
	f1.close()

links()