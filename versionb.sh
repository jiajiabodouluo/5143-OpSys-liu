#!/bin/bash
# get the file name
passed_file=$1
# get the name wihout .txt
base_name=$(basename $passed_file .txt)
# get date
datatime=$(date -I)
# filename+date+.txt
new_filename=$base_name\_$datatime\.txt
# copy
cp $passed_file $new_filename

