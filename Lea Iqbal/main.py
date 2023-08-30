import time
from sensor import *
#from actuator import *
from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
lcd = LCD()
def safe_exit(signum, frame):
    exit(1)
    
def cleanup():
    # Membersihkan pin GPIO pada Raspberry Pi
    GPIO.cleanup()

try:
    while True:
        print("Tap Kartu")
        signal(SIGTERM, safe_exit)
        signal(SIGHUP, safe_exit)
        lcd.text("tap kartu", 1)
        lcd.text("...", 2)
        status,id=read_rfid()
        if status =="berhasil":
            lcd.text(str(id), 1)
            lcd.text(status, 2)
            time.sleep(1)
        else : 
            lcd.text(str(id), 1)
            lcd.text(status, 2)
            time.sleep(1)

        #time.sleep(0.5)  # Memberi jeda sebelum membaca data berikutnya

except KeyboardInterrupt:
    # Memberhentikan program dengan menekan Ctrl + C
    cleanup()
