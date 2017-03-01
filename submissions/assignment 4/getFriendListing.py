#!.usr/local/bin/python2.7

import sys
from xml.dom.minidom import parseString

def getInfo(xml):

	dom = parseString(xml)
	countDict = {}
	
	for element in dom.getElementsByTagName("data"):
	
		if(element.attributes['key'].value == 'name'):
			name = element.childNodes[0].data
			
		if(element.attributes['key'].value == 'friend_count'):
			count = element.childNodes[0].data
			
			countDict[name] = count
			name = ''
			count = ''
			
	return countDict
	
def getCount(xml):

	dom = parseString(xml)
	return len(dom.getElementsByTagName("node"))
	
if __name__ == "__main__":

	friendDataFile = sys.argv[1]
	
	f = open(friendDataFile)
	xml = f.read()
	f.close()
	
	friendCount = getCount(xml)
	friendInfo = getInfo(xml)
	
	print("Name, Friend Count")
	print('PROF MLN, ' + str(friendCount))
	
	for friend in friendInfo:
		print(friend + ', ' + friendInfo[friend])