# run this command to setup port for rfid
# replace ttyUSB0 with port name
# sudo stty -F /dev/ttyUSB0 9600 time 2 min 100 -hupcl brkint ignpar -icrnl -opost -onlcr -isig -icanon -echo

import os

os.popen("sudo stty -F /dev/ttyUSB0 9600 time 2 min 100 -hupcl brkint ignpar -icrnl -opost -onlcr -isig -icanon -echo")

def read_rfid():
    print("Bring RFID Tag Near the Scanner")
    string = str(os.popen("sudo head -c 12 /dev/ttyUSB0").read())
    print(string)
    return string


# read_rfid()