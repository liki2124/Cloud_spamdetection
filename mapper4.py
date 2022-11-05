import sys
#! /usr/bin/python
import os
from math import log10,sqrt


detection =10.0

for line in sys.stdin:
    line = line.strip()
    sf,nNm= line.split('\t',1)
    Word, Filename = sf.split(' ',1)
    n,N,m = nNm.split(' ',2)
    n = float(n)
    N = float(N)
    m = float(m)
    tfidf = (n/N)*log10(detection/m)
    print('%s %s %s' % (sf,tfidf))