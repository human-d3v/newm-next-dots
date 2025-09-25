#!/usr/bin/env bash

# set destination directory
DIR="$HOME/Pictures/Screenshots"

#make sure directory exists
if [[ ! -d "$DIR" ]]; then
	mkdir -p "$DIR"
fi
DATE_STR=$(date +"%m-%d-%y")
EXTENSION="png"

# list files matching today's date
LAST_INDEX=$(ls $DIR/${DATE_STR}_*.${EXTENSION} 2>/dev/null | \
	sed -E "s/.*${DATE_STR}_([0-9]+)\\.${EXTENSION}$/\\1/" | \
	sort -n | tail -1)

# if no files match LAST_INDEX, start at 1
if [[ -z "$LAST_INDEX" ]]; then 
	INDEX=1
else
	INDEX=$(( $LAST_INDEX + 1 ))
fi

OUTPUT_FILENAME="${DATE_STR}_${INDEX}.${EXTENSION}"

grim -g "$(slurp)" "$DIR/${OUTPUT_FILENAME}"
