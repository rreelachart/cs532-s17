import tweepy
import commands
import json
import time

CONSUMER_KEY = "Vvp6YekJ62nw1SCvx9xNeBUWr"
CONSUMER_SECRET = "2P2bP3i8Ne3kgkFIgFBya3mRHbZgM2MvLTkv1GEDuxMywgPbGw"
OAUTH_TOKEN = "704338593108484096-DFScjuC1jzqT8b2U8rTYByvgPLJbkzi"
OAUTH_TOKEN_SECRET = "zrKA3L2astz0ycX1eX42qml5yhBNP4NqqxnqePXLKEbW1"

auth = tweepy.auth.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

f2 = open('twitterLinksData', 'w')
	
def getAllLinks():
	read = open('sourceTarget','r')	
	data= json.load(read)
	for user in data:
		dict= {}
		sourceScreenName= user["source"]
		targetScreenName= user["target"]
		result = api.show_friendship(source_screen_name=sourceScreenName, target_screen_name=targetScreenName)
		dict['followed_by'] =result[0].followed_by
		dict['following'] =result[0].following
		dict['screen_name1']= result[0].screen_name
		dict['screen_name2']= result[1].screen_name
		f2.write(json.dumps(dict)+",\n")

getAllLinks()