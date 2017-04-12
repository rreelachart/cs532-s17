import clusters

def getKmeans():
	blognames,words,data=clusters.readfile('blogTermMatrix.txt') 
	print "Centroid Value: 5"
	kclust=clusters.kcluster(data,k=5)
	print "\t\t"+str([blognames[r] for r in kclust[0]]) # Print blognames in 1st centroid
	print "\t\t"+str([blognames[r] for r in kclust[1]]) # Print blognames in 2nd centroid
	print "\t\t"+str([blognames[r] for r in kclust[2]]) # And so on and so forth
	print "\t\t"+str([blognames[r] for r in kclust[3]]) 
	print "\t\t"+str([blognames[r] for r in kclust[4]]) 
	print "Centroid Value: 10"
	kclust=clusters.kcluster(data,k=10)
	print "\t\t"+str([blognames[r] for r in kclust[0]]) 
	print "\t\t"+str([blognames[r] for r in kclust[1]])
	print "\t\t"+str([blognames[r] for r in kclust[2]])
	print "\t\t"+str([blognames[r] for r in kclust[3]]) 
	print "\t\t"+str([blognames[r] for r in kclust[4]]) 
	print "\t\t"+str([blognames[r] for r in kclust[5]]) 
	print "\t\t"+str([blognames[r] for r in kclust[6]]) 
	print "\t\t"+str([blognames[r] for r in kclust[7]]) 
	print "\t\t"+str([blognames[r] for r in kclust[8]]) 
	print "\t\t"+str([blognames[r] for r in kclust[9]]) 
	print "Centroid Value: 20"
	kclust=clusters.kcluster(data,k=20)
	print "\t\t"+str([blognames[r] for r in kclust[0]]) 
	print "\t\t"+str([blognames[r] for r in kclust[1]]) 
	print "\t\t"+str([blognames[r] for r in kclust[2]])
	print "\t\t"+str([blognames[r] for r in kclust[3]]) 
	print "\t\t"+str([blognames[r] for r in kclust[4]]) 
	print "\t\t"+str([blognames[r] for r in kclust[5]]) 
	print "\t\t"+str([blognames[r] for r in kclust[6]]) 
	print "\t\t"+str([blognames[r] for r in kclust[7]]) 
	print "\t\t"+str([blognames[r] for r in kclust[8]]) 
	print "\t\t"+str([blognames[r] for r in kclust[9]]) 
	print "\t\t"+str([blognames[r] for r in kclust[10]]) 
	print "\t\t"+str([blognames[r] for r in kclust[11]])
	print "\t\t"+str([blognames[r] for r in kclust[12]]) 
	print "\t\t"+str([blognames[r] for r in kclust[13]]) 
	print "\t\t"+str([blognames[r] for r in kclust[14]]) 
	print "\t\t"+str([blognames[r] for r in kclust[15]]) 
	print "\t\t"+str([blognames[r] for r in kclust[16]]) 
	print "\t\t"+str([blognames[r] for r in kclust[17]]) 
	print "\t\t"+str([blognames[r] for r in kclust[18]]) 
	print "\t\t"+str([blognames[r] for r in kclust[19]]) 
	
getKmeans()