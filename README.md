# weatherFlow-alerter
Python scripts I wrote to generate alerts from weatherflow data

If using multiple alert scripts, it is best to cache the json data to a file.  To do this, I set a command in cron to dump data from the API to a local file: /scripts/wxresult  You can run this on a VM or even a raspberry pi computer board.

# Cron:
```
*/2 * * * *   root    /usr/bin/curl "https://swd.weatherflow.com/swd/rest/observations/station/73221?token=<put your Weatherflow API token here>" > /scripts/wxresult
```
