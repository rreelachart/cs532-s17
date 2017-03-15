library(igraph)
library(igraphdata)

data(karate)

club <- karate

plot.igraph(club, 
  vertex.color="purple",
  vertex.frame.color="#000000",
  vertex.shape="circle",
  vertex.size=15,
  vertex.label.color="#ffffff",
  edge.color="black",
  main="Zachary's Karate Club Graph Before Breakup",
  vertex.label.font=2,
  layout=layout.kamada.kawai,
  vertex.label.cex=1.2
)