#/usr/bin/env bash

LOG_FILE="Consumer.log"
LIMIT_LINES=1000

while true; do
    echo Starting validation...
    [ $(wc -l $LOG_FILE | cut -f1 -d" ") -ge $LIMIT_LINES ] && mv $LOG_FILE /tmp/"${LOG_FILE}_$(date +%F_%T)"
    sleep 10;
    echo Process finished!
done