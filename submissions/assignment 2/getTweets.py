#!/usr/local/bin/python3

from __future__ import unicode_literals
import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs
import json
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/authorize"
ACCESS_TOKEN_URL ="https://api.twitter.com/oauth/access_token"

CONSUMER_KEY = "Vvp6YekJ62nw1SCvx9xNeBUWr"
CONSUMER_SECRET = "2P2bP3i8Ne3kgkFIgFBya3mRHbZgM2MvLTkv1GEDuxMywgPbGw"

OAUTH_TOKEN = "704338593108484096-DFScjuC1jzqT8b2U8rTYByvgPLJbkzi"
OAUTH_TOKEN_SECRET = "zrKA3L2astz0ycX1eX42qml5yhBNP4NqqxnqePXLKEbW1"

#If breaks down or something, hopefully this will catch it
class TwitterError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)
		
#Setup app authorization. Code adapted from code found at:
#https://thomassileo.name/blog/2013/01/25/using-twitter-rest-api-v1-dot-1-with-python/
def setup_oauth():
	#Request token
	oauth = OAuth1(CONSUMER_KEY, client_key = CONSUMER_SECRET)
	r = requests.post(url = REQUEST_TOKEN_URL, auth=oauth)
	credentials = parse_qs(r.content)
	
	resource_owner_key = credentials[b'oauth_token'][0].decode(encoding = 'UTF-8')
	resource_owner_secret = credentials[b'oauth_token_secret'][0].decode(encoding = 'UTF-8')
	
	#Authorize
	auth_url = AUTHORIZE_URL + resource_owner_key
	print('Please go here and authorize: ' + auth_url)
	
	verifier = input('Please input the verifiter: ')
	oauth = OAuth1(CONSUMER_KEY, 
					client_secret = CONSUMER_SECRET, 
					resource_owner_key = resource_owner_key,
					resource_owner_secret = resource_owner_secret,
					verifier = verifier)
	
	#Finally, obtain the access token
	r = requests.post(url = ACCESS_TOKEN_URL, auth=oauth)
	credentials = parse_qs(r.content)
	token = credentials[b'oauth_token'][0].decode(encoding = 'UTF-8')
	secret = credentials[b'oauth_token_secret'][0].decode(encoding = 'UTF-8')
	
	return token, secret
	
def get_oauth():
	oauth = OAuth1(CONSUMER_KEY,
					client_secret = CONSUMER_SECRET,
					resource_owner_key = OAUTH_TOKEN,
					resource_owner_secret = OAUTH_TOKEN_SECRET)
					
	return oauth
	
def call_api(ident, oauth, count, screenName):
	url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=" + screenName + "&count=" + str(count) + "&max_id=" + str(ident)
	r = requests.get(url, auth = oauth)
	
	if 'errors' in r:
		raise TwitterError(json.dumps(r.json(), sort_keys = True, ident = 4, separators = (',', ': ')))
	
	return r
	
#Call API and print returned tweets
def print_tweets(startingId, oauth, tweetPerCall, numberCalls, screenName):
	
	ident = startingId

	for i in range(0, numberCalls):
		response = call_api(ident, oauth, tweetPerCall, screenName)
		listSize = len(response.json())
		
		print(listSize)
		
		if listSize == 1:
			raise TwitterError("No more tweets.")
			
		for i in range(0, listSize):
			tweet = response.json()[i]
			ident = str(tweet['id'])
			text = tweet['text']
			print(str(ident) + ":" + str(text))
			
		time.sleep(1)

def usage():
	print("Usage: " + sys.argv[0] + "<startingId><tweetPerCall><apiCalls><screenName>")

if __name__ == "__main__":
	try:
		startingId = sys.argv[1]
		tweetPerCall = int(sys.argv[2])
		apiCalls = int(sys.argv[3])
		screenName = sys.argv[4]
	except IndexError as e:
		usage()
		sys.exit(1)
		
	if not OAUTH_TOKEN:
		token, secret = setup_oauth()
		print("OAUTH_TOKEN: " + token)
		print("OAUTH_TOKEN_SECRET: " + secret)
		print( )
	else:
		oauth = get_oauth()
		
		try:
			print_tweets(startingId, oauth, tweetPerCall, apiCalls, screenName)
		except TwitterError as e:
			sys.stderr.write(e.value)
			sys.exit(254)