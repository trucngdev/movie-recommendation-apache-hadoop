#!/usr/bin/python3
"""reducer.py"""

from operator import itemgetter
import sys

prevUid = None
rated = []
# input comes from STDIN
for line in sys.stdin:
    _line = line.split("\t")
    uid = _line[0]
    #first line
    if prevUid is None:
        prevUid = uid

    if (prevUid == uid):
        rated.append(_line[1])
        print(line.replace("\n",""))
    
    else:
        #assign all other movie of previous user Id to 0
        for i in range(1684):
            if str(i) not in rated:
                print('%s\t%s' % (prevUid,str(i)+'\t'+'0'))
        rated = []
        rated.append(_line[1])
        print(line.replace("\n",""))
        prevUid = uid

#final line
for i in range(10):
    if i not in rated:
        print('%s\t%s' % (prevUid,str(i)+'\t'+'0'))

    
