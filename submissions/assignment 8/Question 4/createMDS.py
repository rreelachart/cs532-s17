import clusters

def createMDS():

    blognames,words,data=clusters.readfile('blogTermMatrix.txt') 
    coords=clusters.scaledown(data)
    clusters.draw2d(coords,blognames,jpeg='mdsCluster.jpg') 
	
createMDS()