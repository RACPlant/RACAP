#!/usr/bin/env bash
# run every 00:00:00

LOG_FILES="Consumer*.log"
LOG_DATE=$(date +%F_%T)
echo Starting backup...
mkdir /tmp/${LOG_DATE}
mv $LOG_FILES /tmp/"${LOG_DATE}/${LOG_FILE}"
echo Process finished!
