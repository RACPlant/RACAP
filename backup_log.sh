/usr/bin/env bash

KB_FILE=kb.pl
LIMIT_LINES=1000

while true; do 
    [ $(wc -l $KB_FILE | cut -f1 -d" ") -ge $LIMIT_LINES ] && mv $KB_FILE /tmp/${KB_FILE}_${date +%F_%T}
    sleep 10;
done