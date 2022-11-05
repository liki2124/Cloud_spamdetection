#! /usr/bin/python
import sys

for line in sys.stdin:
    # remove whitespace
    line = line.strip()
    #splitting line to words
    wordFile,count = line.split(' ',1)
    word,File=wordFile.split(' ',1)
    Z = word+' '+count;
    print ('%s %s' % (File, Z))