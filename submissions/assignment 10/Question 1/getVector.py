import json
f= open('blogTermMatrix.txt','r')
output = open('blogTermVector','w')
list1 = []
count = 0
for line in f:
	count += 1
	if count >1:  
		dict = {}
		line = line.strip()
		list = line.split('\t')
		# print list
		blogName= list[0]
		list.pop(0)
		vector = list
		# print blogName
		# print vector
		dict[blogName] = vector
		list1.append(dict)
output.write(json.dumps(list1))