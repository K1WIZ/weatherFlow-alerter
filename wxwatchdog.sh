#!/bin/bash

check() {
  windwatch=$(pgrep -f windWatch.py | wc -l)
  lightningwatch=$(pgrep -f lightningWatch.py | wc -l)
  uvwatch=$(pgrep -f uvWatch.py | wc -l)
}

while :
do
  check
  if [ "${windwatch}" -lt "1" ]
  then
        /usr/bin/python3 /scripts/windWatch.py 2>>/var/log/wxwatch-err.log 1>>/var/log/wxwatch.log &
        echo "Wind watch restarted - $(date +%Y-%m-%d_%H:%M:%S)" >> /var/log/wxwatch.log
  fi
  if [ "${lightningwatch}" -lt "1" ]
  then
        /usr/bin/python3 /scripts/lightningWatch.py 2>>/var/log/wxwatch-err.log 1>>/var/log/wxwatch.log &
        echo "Lightning Watch Restarted - $(date +%Y-%m-%d_%H:%M:%S)" >> /var/log/wxwatch.log
  fi
  if [ "${uvwatch}" -lt "1" ]
  then
        /usr/bin/python3 /scripts/uvWatch.py 2>>/var/log/wxwatch-err.log 1>>/var/log/wxwatch.log &
        echo "UV Watch Restarted - $(date +%Y-%m-%d_%H:%M:%S)" >> /var/log/wxwatch.log
  fi
  sleep 1
done
