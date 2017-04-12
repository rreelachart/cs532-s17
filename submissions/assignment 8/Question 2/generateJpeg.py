import clusters

def generateJpeg():
	blognames,words,data=clusters.readfile('blogTermMatrix.txt') 
	clust=clusters.hcluster(data) 
	clusters.drawdendrogram(clust,blognames,jpeg='JpegDendrogram.jpg') 

generateJpeg()