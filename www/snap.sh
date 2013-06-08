#!/bin/sh

# Take one picture, add a timestamp to it and possibly rotate it also.
# $1: picture name, $2: rotation angle

cd `dirname $0`/cam
raspistill -w 1280 -h 960 -t 1000 -o snaptemp.jpg
date=`date --rfc-3339=seconds`
echo $date
convert -rotate "$2" \
    -pointsize 15 \
    -draw "text 0 20 \"$date\"" -fill white \
    -draw "text 1 21 \"$date\"" -fill black \
    snaptemp.jpg snaptemp2.jpg
mv -f snaptemp2.jpg $1-now.jpg
