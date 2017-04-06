#!/usr/bin/python2.7

import json

def getTopAndBottom():
	f = open('threeUsers.json','r')
	f1 = open('threeUsersWithMovies.json','w')
	userData = json.load(f)
	dict= {}
	for user in userData:
		dict['user_id'] = user['user_id']
		for movie in user['movie_details']:
			if movie['movie_rating'] =='5':
				dict['type'] ='Top Rated'
				dict['movie_id']=movie['movie_id']
				dict['movie_name']=movie['movie_name']
				dict['movie_rating']=movie['movie_rating']
				f1.write(json.dumps(dict) + ',\n')
			if movie['movie_rating'] =='1':
				dict['type'] ='Least Rated'
				dict['movie_id']=movie['movie_id']
				dict['movie_name']=movie['movie_name']
				dict['movie_rating']=movie['movie_rating']
				f1.write(json.dumps(dict) + ',\n')
				
getTopAndBottom()