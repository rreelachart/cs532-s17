import feedparser
import re
import math
import docclass


# Takes a filename of URL of a blog feed and classifies the entries
def read(feed,classifier):

    splitExpression = re.compile(r"<[^>]+>")
    itemCount = 0
    print "first 50 entry classification"
    # Get feed entries and loop over them
    f=feedparser.parse(feed)

    for item in f['items'][0:49]:
        itemCount = itemCount+1
        print itemCount
        print '-----'

        # Print the contents of the item
        title = item['title'].encode('utf-8')
        print 'Title: '+title

        description = item['description'].encode('utf-8')
        print 'Description:' +description

        # Combine all the text to create one item for the classifier
        fulltext = '%s\n%s' % (item['title'], item['summary'])
        fulltext = fulltext.replace("'","") 
        predictedString = str(classifier.classify(fulltext))

        # Print the best guess at the current category
        print "predicted category",predictedString

        # Ask the user to specify the correct category and train on that
        
        actual =raw_input('Enter the actual category it belongs to: ')        
        classifier.train(fulltext,actual)

    print "entering into another mode"
    itemCount = 49
    print "other 50 item classification"
    # Get feed entries and loop over them
    f=feedparser.parse(feed)
    for item in f['items'][50:100]:
        itemCount = itemCount+1
        print
        print '-----'

        # Print the contents of the item
        title = item['title'].encode('utf-8')
        print 'Title: \t'+title

        description = item['description'].encode('utf-8')
        print 'Description:' +description

        # Combine all the text to create one item for the classifier
        fulltext = '%s\n%s' % (item['title'], item['summary'])
        fulltext = fulltext.replace("'","") 
        predicted= str(classifier.classify(fulltext))

        # Print the best guess at the current category
        print "predicted category",predicted

        # Ask the user to specify the correct category and train on that
        
        actualS =raw_input('Enter the actual category it belongs to: ')
        feature = raw_input('Enter a string to classifier:')


        cprobabilty = round(classifier.cprob(feature,predicted),4)
        print cprobabilty
        
        # classifier.train(fulltext,actual)