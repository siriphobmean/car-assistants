#!/usr/bin/env python3

import serial
import requests
from time import sleep
import RPi.GPIO as GPIO

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pins
led_pins = [5, 6, 12, 13, 19, 16, 26, 20]

# Setup GPIO pins as output
for led_pin in led_pins:
    GPIO.setup(led_pin, GPIO.OUT)
    GPIO.output(led_pin, GPIO.HIGH)
    sleep(0.05)

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

car_license_plate = "นม 6 เลย"

message_start = f'รถยนต์ทะเบียน "{car_license_plate}" ถูกสตาร์ท...'
response_start = send_line_notify(line_notify_token, message_start)
message_location = f'ตำแหน่งของรถยนต์: "มทส. ประตู 4"'
response_location = send_line_notify(line_notify_token, message_location)

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()

    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)

            ser.reset_input_buffer()
            if int(line) <= 6:
                for _ in range(8):
                        for led_pin in led_pins:
                            GPIO.output(led_pin, GPIO.LOW)
                        sleep(0.5)
                        for led_pin in led_pins:
                            GPIO.output(led_pin, GPIO.HIGH)
                        sleep(0.5)
                message_accident = f'รถยนต์ทะเบียน "{car_license_plate}" เกิดอุบัติเหตุ!'
                response_accident = send_line_notify(line_notify_token, message_accident)
                message_location = f'ตำแหน่งของรถยนต์: "มทส. ประตู 1"'
                response_location = send_line_notify(line_notify_token, message_location)
                sleep(0.5)

                if response_accident.status_code == 200:
                    print("Notification sent successfully.")
                else:
                    print(f"Failed to send notification. Status code: {response_accident.status_code}")

        for led_pin in led_pins:
            GPIO.output(led_pin, GPIO.LOW)
            sleep(0.05)