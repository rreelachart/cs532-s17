library(igraph)
library(igraphdata)

data(karate)

club <- karate
#Used for creating the number of groups for the break up. Change to 3,4,5 for extra credit.
grouping <- 2

#Based algorithm off the description given in the Wikipedia article https://en.wikipedia.org/wiki/Girvan%E2%80%93Newman_algorithm. This while loop handles the first two steps mostly.
while( clusters(club)$no < grouping ) {
  #1) The betweenness of all existing edges in the network is calculated first.
  edgeBetweenness <- edge.betweenness(club)
  
  #1.1) Order the collected edges in decreasing order
  decreasingBetweenness <- order(edgeBetweenness, decreasing = TRUE)

  #Credit to: http://stackoverflow.com/questions/652136/how-can-i-remove-an-element-from-a-list for how to delete one element from a list.
  #1.2) Get the edge with the highest betweenness from ordered list.
  highestBetweenness <- decreasingBetweenness[-1]
  
  #1.3) Get the highest betweenness edge from the club.
  edgeToDelete <- get.edge(club, highestBetweenness)
  
  #2.) Delete the edge from the club.
  club <- delete.edges(club, E(club, P = edgeToDelete))
}

plot.igraph(club, 
  vertex.color="green",
  #vertex.color="blue", for 3 grouping
  #vertex.color="red", for 4 grouping
  #vertex.color="pink", for 5 grouping
  vertex.frame.color="#000000",
  vertex.shape="circle",
  vertex.size=15,
  vertex.label.color="#ffffff",
  edge.color="black",
  main="Zachary's Karate Club After Breakup (5 Groups)",
  vertex.label.font=2,
  layout=layout.kamada.kawai,
  vertex.label.cex=1.2
  )