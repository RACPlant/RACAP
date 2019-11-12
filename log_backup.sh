#!/usr/bin/env bash
# run every 00:00:00

LOG_FILES="Consumer*.log"

echo Starting backup...
mv $LOG_FILES /tmp/"$(date +%F_%T)/${LOG_FILE}"
echo Process finished!
