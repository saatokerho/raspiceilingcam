#!/bin/sh

# debug utility for serving just one picture without moving the servos at all

while true; do
	`dirname $0`/snap.sh snap 0
done
