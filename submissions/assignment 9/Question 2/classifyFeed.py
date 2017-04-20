import docclass
import feedfilter

def main():
	print "testing the program1"
	cl=docclass.fisherclassifier(docclass.getwords) 
	print "testing the program2"
	cl.setdb('rreelac.db')
	print "testing the program3"
	feedfilter.read('theEscapist100.xml',cl)
	print "testing the program4"
	
main()