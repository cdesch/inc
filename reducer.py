#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys
from datetime import datetime

current_word = None
current_count = 0
word = None
datemap = {}


# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    #print(line)
    # parse the input we got from mapper.py
    raw_date, count = line.split('\t', 1)
    #print("Hello World")
    #print(word)
    #print(count)

    # convert count (currently a string) to int
    try:
        count = int(count)
        date =  datetime.strptime(raw_date, '%Y-%m-%d')
        datemap[date] = datemap.get(date, 0) + count

    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    # if current_word == word:
    #     current_count += count
    # else:
    #     if current_word:
    #         # write result to STDOUT
    #         print '%s\t%s' % (current_word, current_count)
    #     current_count = count
    #     current_word = word

# do not forget to output the last word if needed!
# if current_word == word:
#     print '%s\t%s' % (current_word, current_count)

# sort the reddits alphabetically;
sorted_datemap = sorted(datemap.items(), key=itemgetter(0))

# output to STDOUT
for date, total_occurances in sorted_datemap:
    print '%s\t%s'% (date.date(), total_occurances)