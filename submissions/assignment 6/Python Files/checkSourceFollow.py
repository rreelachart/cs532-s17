import commands
import json
import time

f1=open('sourceTarget','w')

def getSource():
	read=open('twitterNodes','r')
	data= json.load(read)
	list= []
	for user in range(0,len(data)):
		sourceScreenName= data[user]["screenName"]
		for user1 in range(user,len(data)-1):
			targetScreenName = data[user1+1]["screenName"]
			checkSourceFollowersAndFollowing(sourceScreenName,targetScreenName)
				
def checkSourceFollowersAndFollowing(sourceScreenName,targetScreenName):
	dict= {}
	count = 0
	dict['source']= sourceScreenName
	dict['target']= targetScreenName
	f1.write(json.dumps(dict)+",\n")	
	
getSource()