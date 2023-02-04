import time
import board
from digitalio import DigitalInOut, Direction
import adafruit_fingerprint
import serial
uart = serial.Serial("/dev/serial0", baudrate=57600, timeout=1)
finger = adafruit_fingerprint.Adafruit_Fingerprint(uart)

def get_fingerprint():
    print("Enter FingerPrint")
    if finger.read_templates() != adafruit_fingerprint.OK:
        raise RuntimeError("Failed to read templates")
    while finger.get_image() != adafruit_fingerprint.OK:
        pass
    if finger.image_2_tz(1) != adafruit_fingerprint.OK:
        print("failed")
        return False
    if finger.finger_search() != adafruit_fingerprint.OK:
        print("failed")
        return False
    print("pass")
    return True
 
# while (True):
#     time.sleep(1)
#     if get_fingerprint():
#         print("Detected fingerprint")
#     else:
#         print("Finger not found")

# if get_fingerprint():
# 	print("Detected fingerprint")
# else:
# 	print("Finger not found")