#!/bin/bash
# get doctopmary
dictionary="/usr/share/dict/words"
# get words of dictionary 
lines=$(wc -l $dictionary > cut.txt && cut -d " " -f1 cut.txt)
# random number of line
random=$((RANDOM%$lines+1))
# get the word of the random line
word=$(sed -n "${random}p" $dictionary)

echo $word
