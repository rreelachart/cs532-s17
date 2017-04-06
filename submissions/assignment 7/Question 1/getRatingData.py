#!/usr/bin/python2.7

import json
import re

def getRatingData(path='./movieData/'):
	ratingDataFile = open("ratingData.json","w")
	ratingData ={}
	for line in open(path + 'u.data'):
		(user, movieid, rating, ts) = line.split('\t')
		ratingData['user'] = user.strip()
		ratingData['movieid'] = movieid.strip()
		ratingData['rating'] = rating.strip()
		ratingDataFile.write(json.dumps(ratingData)+",\n")

getRatingData()