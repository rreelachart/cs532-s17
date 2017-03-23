import tweepy
import sys
import json
import time

CONSUMER_KEY = "Vvp6YekJ62nw1SCvx9xNeBUWr"
CONSUMER_SECRET = "2P2bP3i8Ne3kgkFIgFBya3mRHbZgM2MvLTkv1GEDuxMywgPbGw"
OAUTH_TOKEN = "704338593108484096-DFScjuC1jzqT8b2U8rTYByvgPLJbkzi"
OAUTH_TOKEN_SECRET = "zrKA3L2astz0ycX1eX42qml5yhBNP4NqqxnqePXLKEbW1"

auth = tweepy.auth.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

f = open('twitterNodes','w')
def nodes():
	count = 1
	page_count= 0
	userData = []
	for user in tweepy.Cursor(api.followers, screen_name='ODUFootballCamp').items():
		usr = {}
		usr['screenName'] = user.screen_name
		usr['name'] =  user.name
		usr['id'] =  count
		usr['img'] =  user.profile_image_url
		usr['link'] = "https://twitter.com/"+user.screen_name
		usr['size'] =  40000
		page_count += 1
		userData.append(usr)
		count+= 1
	f.write(json.dumps(userData)+"\n")
	f.close()

nodes()