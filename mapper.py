#!/usr/bin/env python
"""mapper.py"""

import sys
from datetime import datetime

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    line = line.split(",")

    if len(line) >=2:
      raw_date = line[0]
      ticket_num = line[1]
      #ValueError: time data '\xef\xbb\xbf from encoding -> https://stackoverflow.com/questions/18664712/split-function-add-xef-xbb-xbf-n-to-my-list
      date = datetime.strptime(raw_date, '%m/%d/%y %I:%M %p')
      
      print '%s\t%s' % (date.date(), ticket_num)
    # # increase counters
    # for word in words:
    #     # write the results to STDOUT (standard output);
    #     # what we output here will be the input for the
    #     # Reduce step, i.e. the input for reducer.py
    #     #
    #     # tab-delimited; the trivial word count is 1
    #     print '%s\t%s' % (word, 1)