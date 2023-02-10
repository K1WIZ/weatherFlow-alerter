import json
import datetime
import subprocess
import time
import smtplib

condition_flag = 0
def check_uv():
    global condition_flag

    while True:
        try:
            with open('/scripts/wxresult', 'r') as f:  # pickup json data from temp file
                try:
                    data = json.load(f)
                except json.decoder.JSONDecodeError as e:
                    print("Error reading JSON data from file '/scripts/wxresult':", e)
                    time.sleep(2)
                    continue
                break
        except FileNotFoundError as e:
            print("Error opening file '/scripts/wxresult':", e)
            time.sleep(2)
            continue
        break

    try:
        uv_level = data['obs'][0]['uv']
        if uv_level >= 10:      # Set UV threshold here
            now = datetime.datetime.now()
            from_address = "" # Set your FROM address here
            to_address = "" # Set your destination address here
            subject = f"Dangerous UV Alert: ({now.strftime('%m-%d-%Y %I:%M %p')})"
            message = f"THIS IS AN AUTOMATED WARNING - DO NOT REPLY \nWeather sensors have detected DANGEROUS UV LEVELS at or greater \
than {uv_level}  in our neighborhood.  If outdoors or poolside, please consider moving to safe shelter. \
Re-assess conditions after 1 hour from the time of this alert.  If no more alerts are received after 1 hour has passed, conditions \
should have expired and you should proceed outdoors with caution.  If conditions have not expired within 1 hour from this alert, \
you will receive another message if the unsafe condition is continued 1 hour from now\n\nPlease tune in to local broadcast outlets to \
get the latest information on weather conditions.  \n\nSTAY SAFE!"
            smtp_server = ""  # Put your SMTP relay here
            email_message = f"From: {from_address}\nTo: {to_address}\nSubject: {subject}\n\n{message}"
            with smtplib.SMTP(smtp_server) as server:
                server.sendmail(from_address, to_address, email_message)
            condition_flag = 1
        else:
            condition_flag = 0
    except KeyError:
        print("KeyError: Requested key not found in API response")

while True:
    now = datetime.datetime.now()
    next_hour = now.replace(minute=0, second=0, microsecond=0) + datetime.timedelta(hours=1)
    wait_time = (next_hour - now).total_seconds()
    if condition_flag == 1:
        time.sleep(wait_time)
    else:
        time.sleep(2)
    check_uv()
