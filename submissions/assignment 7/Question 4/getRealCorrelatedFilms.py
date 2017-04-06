#!/usr/bin/python2.7

import json
import re
from math import sqrt
import sys
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

def topMatches(prefs,person,n=5,similarity=sim_pearson,reverseSimilarityFlag=True):
  scores=[(similarity(prefs,person,other),other) 
                  for other in prefs if other!=person]
  scores.sort()
  
  if(reverseSimilarityFlag):
  
	scores.reverse()
  upperLimit = len(scores)
  lowerLimit = upperLimit - 5
  upperScores = scores[0:5]
  lowerScores = scores[lowerLimit:upperLimit]
  scoreResult = []
  for item in upperScores:
    scoreResult.append(item)
  for item in lowerScores:
    scoreResult.append(item)

  return scoreResult

def transformPrefs(prefs):
  result={}
  for person in prefs:
    for item in prefs[person]:
      result.setdefault(item,{})
      
      result[item][person]=prefs[person][item]
  return result


def calculateSimilarItems(prefs, movieName, simMeasure, n=10, reverseSimilarityFlag=True, transformMatrixFlag=True):

    result = {}

    if( transformMatrixFlag ):
        itemPrefs = transformPrefs(prefs)
    else:
        itemPrefs = prefs

    for item in itemPrefs:
	    
        scores = topMatches(itemPrefs, item, n=n, similarity=simMeasure, reverseSimilarityFlag=reverseSimilarityFlag)     
        result[item] = scores
        if item.lower() in movieName.lower():
		    return result
    return result

def loadMovieLens(path='./movieData'):
  movies={}
  for line in open(path+'/u.item'):
    (id,title)=line.split('|')[0:2]
    movies[id]=title
  prefs={}
  count = 0
  for line in open(path+'/u.data'):
    (user,movieid,rating,ts)=line.split('\t')
    prefs.setdefault(user,{})
    prefs[user][movies[movieid]]=float(rating)
  return prefs, movies

#Bottom Movie "8 Heads in a Duffel Bag"
movieLensRating, moviesData = loadMovieLens()
MOVIE_NAME=moviesData['1664']
result1 = calculateSimilarItems(movieLensRating, MOVIE_NAME,simMeasure=sim_pearson, n=10, reverseSimilarityFlag=True, transformMatrixFlag=True) 
item = result1[MOVIE_NAME]
print 'Top five correlated films for: ', MOVIE_NAME
for film in item[0:5]:
    print film
print 'Bottom five correlated films for: ', MOVIE_NAME
for film in item[5:10]:
    print film

#Top Movie "Hercules"
MOVIE_NAME=moviesData['993']
result1 = calculateSimilarItems(movieLensRating, MOVIE_NAME,simMeasure=sim_pearson, n=10, reverseSimilarityFlag=True, transformMatrixFlag=True) 
item = result1[MOVIE_NAME]
print 'Top five correlated films for: ', MOVIE_NAME
for film in item[0:5]:
    print film
print 'Bottom five correlated films for: ', MOVIE_NAME
for film in item[5:10]:
    print film