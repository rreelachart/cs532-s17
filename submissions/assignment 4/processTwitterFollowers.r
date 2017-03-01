#!/usr/bin/Rscript

args <- commandArgs(trailingOnly = TRUE)

inputListing <- args[1]
outputGraph <- args[2]
listLength <- as.integer(args[3])
indicator <- args[4]

data <- read.csv(inputListing)

sortedData <- sort(data$Friend.Count)

meanText <- paste("Mean: ", mean(sortedData), collapse = "")

medianText <- paste("Median: ", median(sortedData), collapse = "")

sdText <- paste("Std Dev: ", sd(sortedData), collapse = "")

write(meanText, stdout())
write(medianText, stdout())
write(sdText, stdout())

pdf(outputGraph)

pos <- (sortedData == listLength)
cols <- c("white", "red")

barplot(sortedData, main="Followers of MLN's Followers on Twitter", xlab="Followers by increasing number of followers", ylab="Number of followers", col=cols[pos + 1], ylim=c(0, max(sortedData) + 100))

text(x=match(c(listLength), sortedData) + 20, y=max(sortedData) - 100, labels=indicator, col='red')

arrows(x0=match(c(listLength), sortedData) + 20, y0=(max(sortedData) - 400), x1=match(c(listLength), sortedData) + 20, y1=300, length=0.1, lwd=3, col='red')

dev.off()