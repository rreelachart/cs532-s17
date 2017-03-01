#!/usr/bin/Rscript

args <- commandArgs(trailingOnly = TRUE)

inputListing <- args[1]
outputGraph <- args[2]
listLength <- args[3]
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

barplot(sortedData, main="Friends of MLN's Friends on Facebook", xlab="Friends by increasing number of friends", ylab="Number of friends", col=cols[pos + 1], ylim=c(0, max(sortedData) + 100))

text(x=match(c(listLength), sortedData) + 8, y=max(sortedData), labels=indicator, col='red')

arrows(x0=match(c(listLength), sortedData) + 8, y0=(max(sortedData) - 50), x1=match(c(listLength), sortedData) + 8, y1=175, length=0.1, lwd=3, col='red')

dev.off()