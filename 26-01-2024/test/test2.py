#!/usr/bin/env python3

import serial
import requests

def send_line_notify(token, message):
    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    payload = {"message": message}
    response = requests.post(url, headers=headers, params=payload)
    return response

# Line Notify Token
line_notify_token = "xJMlwJPQ7qC9gwrtq2G0T9nmQ75ii3YISEhbbDrQItz"

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()

    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)

            if line == "12":
                message = "Value is 12. Sending notification to Line Notify."
                response = send_line_notify(line_notify_token, message)

                if response.status_code == 200:
                    print("Notification sent successfully.")
                else:
                    print(f"Failed to send notification. Status code: {response.status_code}")
