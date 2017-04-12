import clusters

def generateJpeg():
	blognames,words,data=clusters.readfile('blogTermMatrixTFIDF.txt') 
	clust=clusters.hcluster(data) 
	clusters.drawdendrogram(clust,blognames,jpeg='JpegDendrogramTFIDF.jpg') 

generateJpeg()