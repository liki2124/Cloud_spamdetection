#! /usr/bin/python
import sys
import os

stopwords= ['a','able','about','across','after','all','almost','also','am','among','an','and','any','are','as','at','be','because','been','but','by',
            'can','cannot','could','dear','did','do','does','either','else','ever','every','for','from','get','got','had','has','have','he','her','hers',
            'him','his','how','however','i','if','in','into','is','it','its','just','least','let','like','likely','may','me','might','most','must','my',
            'neither','no','nor','not','of','off','often','on','only','or','other','our','own','rather','said','say','says','she','should','since','so',
            'some','than','that','the','their','them','then','there','these','they','this','tis','to','too','twas','us','wants','was','we','were','what',
            'when','where','which','while','who','whom','why','will','with','would','yet','you','your'];
# input comes from STDIN (standard input)
for line in sys.stdin:
    # filename = os.environ["map_input_file"]
    userId, text = line.split(',', 1)
    # remove leading and trailing whitespace
    text = text.strip()
    # split the line into words
    words = text.split()
    # increase counters
    for word in words:
        word=word.lower();
        if word not in stopwords:
            z=word+' '+userId;
            print ('%s %s' % (z, 1))
