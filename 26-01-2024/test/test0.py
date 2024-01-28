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

# ข้อความที่ต้องการส่ง
message = "Hello, World"

# ส่งข้อความไปยัง Line Notify
response = send_line_notify(line_notify_token, message)

# ตรวจสอบว่าส่งสำเร็จหรือไม่
if response.status_code == 200:
    print("ส่งข้อความสำเร็จ!")
else:
    print(f"เกิดข้อผิดพลาด: {response.status_code}, {response.text}")
