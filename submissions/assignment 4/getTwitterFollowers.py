#!/usr/local/bin/python2.7

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
	
def call_api_for_followers(oauth, count, screenName, cursor):
	url = "https://api.twitter.com/1.1/followers/list.json?screen_name=" + screenName + "&count=" + str(count) + "&cursor=" + cursor
	
	response = requests.get(url, auth=oauth)
	
	if 'errors' in response:
		raise TwitterError(json.dumps(response.json(), sort_keys=True,indent=4, separators=(',', ': ')))
				
	return response
	 
def print_friend_counts(oauth, numberCalls, count, screenName):
	cursor="-1"
	
	print("Name, Friend Count")
	
	followers_count = 0
	
	for i in range(0, numberCalls):
		response = call_api_for_followers(oauth, count, screenName, cursor)
		
		for entry in response.json()['users']:
			ident = str(entry['screen_name'])
			followers = str(entry['followers_count'])
			print(ident + ', ' + followers)
			followers_count += 1
			
		print(screenName + ', ' + str(followers_count))

def usage():
	print("Usage: " + sys.argv[0] + "<apiCalls><screenName>")

if __name__ == "__main__":
	try:
		apiCalls = int(sys.argv[1])
		screenName = sys.argv[2]
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
		count = 200
		
		try:
			print_friend_counts(oauth, apiCalls, count, screenName)
		except TwitterError as e:
			sys.stderr.write(e.value)
			sys.exit(254)