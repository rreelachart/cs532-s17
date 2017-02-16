#!/usr/local/bin/python2.7

import sys
import os
from BeautifulSoup import BeautifulSoup

#Credit to: http://stackoverflow.com/questions/9662346/python-code-to-remove-html-tags-from-a-string
def processHTML(rawHTML):
	cleantext = BeautifulSoup(rawHTML).text
	return cleantext
	
#Credit to: http://stackoverflow.com/questions/9765227/python-ioerror-errno-2-no-such-file-or-directory
#Credit to: http://stackoverflow.com/questions/2424000/read-and-overwrite-a-file-in-python
if __name__ == "__main__":
	dirName = sys.argv[1]
	
	for file in os.listdir(dirName):
		src_path = os.path.join(dirName, file)
		with open(src_path, 'r+') as workingFile:
			rawHTML = workingFile.read()
			procHTML = processHTML(rawHTML)
			#print(procHTML)
			workingFile.seek(0)
			workingFile.write(procHTML)
			workingFile.truncate()
			#workingFile.close()