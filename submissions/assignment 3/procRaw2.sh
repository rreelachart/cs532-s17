#!/bin/bash
#Credit to: http://stackoverflow.com/questions/20895946/syntax-error-near-unexpected-token-bash
#for figuring how to get the past the 'unexpected syntax error /r'
mkdir ProcFiles
for file in *.raw
do
	lynx -dump -force_html $file > ./ProcFiles/$file.proc
done