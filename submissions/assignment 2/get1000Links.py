#!usr/local/bin/python3

import random
import sys

inputfile = sys.argv[1]

f = open(inputfile)
links = f.readlines()
f.close()

count = 1000

selectedLinks = []

while count > 0:
	index = random.randint(0, len(links) - 1)
	newlink =links[index].strip()
	
	if newlink not in selectedLinks:
		selectedLinks.append(newlink)
		count -= 1
		
for link in sorted(selectedLinks):
	print(link)