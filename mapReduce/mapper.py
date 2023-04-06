#!/usr/bin/python3
"""mapper.py"""
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    _line = line.split("\t")
    uid = _line[0]
    val= _line[1]+"\t"+_line[2]
    print ('%s\t%s' % (uid, val))
