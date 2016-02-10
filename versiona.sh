#!/bin/bash

# get file name
passed_file=$1
# get date
datetime_date=$(date -I)
#  date+ filename
new_filename=$datetime_date\_$passed_file
# copy
cp $passed_file $new_filename
