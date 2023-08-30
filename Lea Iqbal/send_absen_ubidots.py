import time
import requests
import math
import random
 
TOKEN = "BBFF-H1uy3f0Fy0VxetmckIztdaM60BZbbb"
DEVICE_LABEL = "presensi-absen"
VARIABLE_1 = "presensi"
 
def build_payload(variable_1,nama,kelas,waktu):
    payload = {variable_1:{"value": 1, "context": {"nama": nama, "kelas": kelas, "waktu": waktu}}}
    return payload
def kirim_data(payload):
    url = "http://industrial.api.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url,DEVICE_LABEL)
    headers = {"X-Auth-Token":TOKEN,"Content-Type":"application/json"}
    status = 400
    attempts = 0
    while status >= 400 and attempts<=5:
        req = requests.post(url=url,headers=headers,json=payload)
        status = req.status_code
        attempts +=1
        time.sleep(1)
   
    print(req.status_code, req.json())
   
    if status>=400:
        print("Ada Error")
        return False
    print("berhasil")
    return True
 
def send_to_ubidots(nama,kelas,waktu):
    payload = build_payload(VARIABLE_1,nama,kelas,waktu)
    print("mencoba mengirim data")
    kirim_data(payload)
 
