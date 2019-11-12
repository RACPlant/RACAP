#!/usr/bin/env bash
# run every 00:00:00

LOG_FILE="Consumer.log"

echo Starting backup...
mv $LOG_FILE /tmp/"${LOG_FILE}_$(date +%F_%T)"
echo Process finished!
