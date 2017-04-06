#!/usr/bin/python2.7

import json
import re
from math import sqrt

def sim_pearson(pref,p1,p2):
  si={}
  for item in pref[p1]: 
    if item in pref[p2]: si[item]=1

  if len(si)==0: return 0

  n=len(si)
    
  sum1 = 0
  for it in si:
	sum1 =  sum1 + int(pref[p1][it])

  sum2 = 0
  for it in si:
	sum2 =  sum2 + int(pref[p2][it])

  sum1Sq = 0
  for it in si:
	sum1Sq =  sum1Sq + pow(int(pref[p1][it]),2)
  
  sum2Sq = 0
  for it in si:
	sum2Sq =  sum2Sq + pow(int(pref[p2][it]),2)

  pSum = 0  
  for it in si:
	pSum =  pSum + ( int(pref[p2][it]) * int(pref[p1][it]) )
	
  num=pSum-(sum1*sum2/n)
  den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
  if den==0: return 0

  r=num/den

  return r

def getRecommendations(prefs,person,similarity=sim_pearson):
  totals={}
  simSums={}
  for other in prefs:
    if other==person: continue
    sim=similarity(prefs,person,other)

    if sim<=0: continue
    for item in prefs[other]:
	    
      if item not in prefs[person] or prefs[person][item]==0:
        totals.setdefault(item,0)
        totals[item] += int(prefs[other][item])*sim
        simSums.setdefault(item,0)
        simSums[item]+=sim

  rankings=[(total/simSums[item],item) for item,total in totals.items()]

  rankings.sort()
  rankings.reverse()
  return rankings

def correlation():
	userDataFile = open("userData.json","r")
	userData = json.load(userDataFile)
	
	correlation_dic = {}
	for user in userData:
		user_id = user['user_id']
		movie_details_dic = {}
		for movie in user['movie_details']:
			movie_id = movie['movie_id']
			movie_rating = movie['movie_rating']
			movie_details_dic[movie_id] = movie_rating
		correlation_dic[user_id] = movie_details_dic
	
	return correlation_dic	

	
def getMovieName(id):
	moviesDataFile = open("movieData.json","r")
	movieData = json.load(moviesDataFile)
	for user in movieData:
		if user['movie_id'] == id:
			print user['movie_id']
			print user['movie_name']
				
correlation_dic = correlation()
user_min = []
user_max = []
max = [-10,-10,-10,-10,-10]
min = [10,10,10,10,10]
for user in correlation_dic:	
	if(user != '429'):
		result = sim_pearson(correlation_dic, '429', user)
		if(max[0] < result):
			max[0] = result
			max.sort()
			user_max.append(user)
		if(min[0] > result):
			min[0] = result
			min.sort()
			min.reverse()
			user_min.append(user)
			
result= getRecommendations(correlation_dic, '429', similarity = sim_pearson) 

Top_Movies=result[0:5]
Least_Movies=result[-5:]
print Top_Movies
print Least_Movies

for movie in Top_Movies:
	getMovieName(movie[1])

for movie in Least_Movies:
	getMovieName(movie[1])