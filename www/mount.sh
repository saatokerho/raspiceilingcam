#!/bin/sh

# I'm using a small ramdisk for the pictures. This may be premature
# optimization, but I still prefer this to a broken SD card some day. The
# ramdisk might also be faster if there are many of users viewing the pics
# simultaneously.

mkdir -p `dirname $0`/cam
mount -t tmpfs tmpfs `dirname $0`/cam -o size=10M
