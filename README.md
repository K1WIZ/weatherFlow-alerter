# weatherFlow-alerter
Python scripts I wrote to generate e-mail alerts from my weatherflow tempest weather data

If using multiple alert scripts, it is best to cache the json data to a file and have the watchdog scripts read relevant data from the file.  This minimizes your API calls.  To do this, I set a command in cron to dump data from the API to a local file: /scripts/wxresult  You can run this on a VM, docker container, or even a raspberry pi computer board.

# Cron:
```
*/2 * * * *   root    /usr/bin/curl "https://swd.weatherflow.com/swd/rest/observations/station/<station ID>?token=<put your Weatherflow API token here>" > /scripts/wxresult
@reboot       root    /scripts/wxwatchdog.sh &
```
