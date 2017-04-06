#!/usr/bin/python2.7

import json
import re

def getMovieData(path='./movieData/'):
	moviesDataFile = open("movieData.json","w")
	movies = {}
	for line in open(path + 'u.item'):
		movie_id = line.split('|')[0:1][0]
		movie_name = line.split('|')[1:2][0]
		movies['movie_id'] = re.sub(r'[^\x00-\x7F]',' ', movie_id)
		movies['movie_name'] = re.sub(r'[^\x00-\x7F]',' ', movie_name)
		moviesDataFile.write(json.dumps(movies) + ',\n')	
	
getMovieData()