import http.client
import urllib.parse

def send_line_notify(token, message):
    url = "/api/notify"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    payload = urllib.parse.urlencode({"message": message})
    
    conn = http.client.HTTPSConnection("notify-api.line.me")
    conn.request("POST", url, payload, headers)
    response = conn.getresponse()
    
    return response

line_notify_token = "K5jvpbiJyIvJfgGr4CpoyNqGnzePRoVpHY0mFylp9SV"

choice = input("ป้อน 1 เพื่อส่งข้อความเริ่มต้น, หรือ 2 เพื่อส่งข้อความเมื่อเกิดอุบัติเหตุ: ")

if choice == "1":
    car_license_plate = "อส 523354 นครราชสีมา"
    place_name = "อาคารเรียนรวม 1"
    lat, lon = 14.881037676495998, 102.01720981012612
    google_maps_link = f'google.com/maps?q={lat},{lon}'
    # message_start = f'🚕🚗🚙\nรถยนต์ทะเบียน\n"{car_license_plate}"\nสถานะ: ถูกสตาร์ท...✅\nตำแหน่ง: {place_name}\n{google_maps_link}'
    message_start = f'🚕🚗🚙\nรถยนต์ทะเบียน\n"{car_license_plate}"\nสถานะ: ถูกสตาร์ท...✅'
    response_start = send_line_notify(line_notify_token, message_start)
    
    if response_start.status == 200:
        print("ส่งข้อความเริ่มต้นสำเร็จ!")
    else:
        print(f"เกิดข้อผิดพลาด: {response_start.status}, {response_start.reason}")

elif choice == "2":
    car_license_plate = "อส 523354 นครราชสีมา"
    place_name = "วงเวียนมหาวิทยาลัย"
    lat, lon = 14.883795262391775, 102.02460500201975
    google_maps_link = f'google.com/maps?q={lat},{lon}'
    # message_accident = f'🚕🚗🚙\nรถยนต์ทะเบียน\n"{car_license_plate}"\nสถานะ: เกิดอุบัติเหตุ🚨❗\nตำแหน่ง: {place_name}\n{google_maps_link}'
    message_accident = f'🚕🚗🚙\nรถยนต์ทะเบียน\n"{car_license_plate}"\nสถานะ: เกิดอุบัติเหตุ🚨❗'
    response_accident = send_line_notify(line_notify_token, message_accident)

    if response_accident.status == 200:
        print("ส่งข้อความเมื่อเกิดอุบัติเหตุสำเร็จ!")
    else:
        print(f"เกิดข้อผิดพลาด: {response_accident.status}, {response_accident.reason}")

else:
    print("ป้อนค่าไม่ถูกต้อง โปรแกรมจบการทำงาน")
