#!/usr/bin/env python
import RPi.GPIO as GPIO
from datetime import datetime
from cek_db import cek_id
from send_absen_ubidots import send_to_ubidots
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()

def read_rfid():
    id, text = reader.read()
    print(id)
    print(text)
    data,status=cek_id(id)
    if status==True:
        now=datetime.now()
        waktu=now.strftime("%d/%m/%Y, %H:%M:%S")
        print(data["kelas"])
        send_to_ubidots(data["nama"],data["kelas"],waktu)
        print("Berhasil Presensi")
        status="berhasil"
        return status,id
    else : 
        print("Kartu tidak terdaftar")
        status="gagal"
        return status,id

