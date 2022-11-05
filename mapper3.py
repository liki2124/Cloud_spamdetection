#! /usr/bin/python
import sys
import os

for line in sys.stdin:
    #remove whitespace
    line = line.strip()
    #remove line to words
    sf,nN =line.split('\t',1)
    s,f=sf.split(' ',1)
    Z=f+' '+nN+' '+str(1)
    print ('%s %s' % (s, Z))