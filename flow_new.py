########################LIBRARIES########################


import cam
from check_fingerprint import get_fingerprint
from upload import sheetsupdate
import RPi.GPIO as GPIO 
from validate import vali
import os
import oled
import time


########################LIBRARIES########################




########################GPIO_SETUP########################


rs_1 = 17
buzzout_button = 6
lock=0
buzzer=22
red_led=23
green_led=24
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer,GPIO.OUT) #Set Buzzer Pin to Output
GPIO.setup(red_led,GPIO.OUT) #Set Red_Led Pin to Output
GPIO.setup(green_led,GPIO.OUT) #Set Green_Led Pin to Output
GPIO.setup(lock,GPIO.OUT)
GPIO.setup(rs_1, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Set Reed Switch 1 Pin to Input with Internal Pull Up Resistor
GPIO.setup(buzzout_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(lock,GPIO.HIGH)

os.popen("sudo stty -F /dev/ttyUSB0 9600 time 2 min 100 -hupcl brkint ignpar -icrnl -opost -onlcr -isig -icanon -echo")


########################GPIO_SETUP########################




################_INTERUPT_CREATE_DESTROY_################

global intcreated
intcreated = False
global intruder
intruder = False

def interupt_create():
    print("interupt_create called")
    global intcreated
    if(intcreated==False):
        print("interupt_create true")
        GPIO.add_event_detect(rs_1, GPIO.RISING, callback=intrusion, bouncetime=300)
        GPIO.add_event_detect(buzzout_button, GPIO.RISING, callback=buzzout, bouncetime=300)
        print("interupt_create called")
        intcreated = True



def interupt_destroy():
    global intcreated
    GPIO.remove_event_detect(rs_1)
    GPIO.remove_event_detect(buzzout_button)
    print("interupt_destroy called")
    intcreated = False


################_INTERUPT_CREATE_DESTROY_################




###############INTRUSION_ALARM###############


def intrusion(aaaa):
    print(aaaa)
    global intruder
    intruder = True
    cam.capture()
    interupt_destroy()
    print("Intruder Detected")
    oled.intruder()
    # GPIO.output(siren,GPIO.LOW)
    for i in range(10):
        GPIO.output(buzzer,GPIO.HIGH)
        GPIO.output(red_led,GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(buzzer,GPIO.LOW)
        GPIO.output(red_led,GPIO.LOW)
        time.sleep(0.2)
    print("end of siren")
    oled.home()
    time.sleep(1.5)
    interupt_create()
    print("int cre")
    # intruder=False
    print("intfalse")
    # loop_var=False
    print("intfalse")
    intruder=False
    print("intfalse")
    
    
    


###############INTRUSION_ALARM###############

door_open_time=2

def open_door():
    print("opening door")
    interupt_destroy()
    GPIO.output(lock,GPIO.LOW)
    GPIO.output(green_led,GPIO.HIGH)
    time.sleep(door_open_time)
    GPIO.output(lock,GPIO.HIGH)
    GPIO.output(green_led,GPIO.LOW)
    interupt_create()


def buzzout(bbbb):
    print(bbbb)
    print("buzzout")
    oled.buzzout()
    interupt_destroy()
    GPIO.output(lock,GPIO.LOW)
    GPIO.output(green_led,GPIO.HIGH)
    sheetsupdate("-","-","-","-","Buzzout")
    time.sleep(door_open_time)
    GPIO.output(lock,GPIO.HIGH)
    GPIO.output(green_led,GPIO.LOW)
    interupt_create()
    print("end of buzzout")



#####################MAIN_TRY_EXCEPT#####################


def main():
    interupt_create()
    if(intruder==False):
        print("intruder = false + ",intruder)
        while (intruder==False):
            print("Normal Loop")
            print("Place your Card On the RFID Scanner")
            oled.home()
            print("main loop card read")
            rfid_tag_id=str(os.popen("sudo head -c 12 /dev/ttyUSB0").read())
            cam.capture()
            if(rfid_tag_id=="75005339405F"):

                oled.welc("Admin","Admin","Admin")
                sheetsupdate("ADMIN","ADMIN","ADMIN",rfid_tag_id,"Admin Card")
                print("admin card entered")
                open_door()
            elif((intruder==False)):
                oled.home()
                print("normal loop card read")
                GPIO.output(green_led,GPIO.HIGH)
                time.sleep(0.75)
                GPIO.output(green_led,GPIO.LOW)
                # cam.capture()
                print(rfid_tag_id)
                tag_valid=False
                id=vali(rfid_tag_id)
                if(len(id) > 0):
                    tag_valid=True
                    print(id)
                    print("a")
                    oled.welc(id[0],id[1],id[2])
                elif(len(id) == 0 ):
                    oled.invalid_card()
                    for i in range(10):
                        GPIO.output(buzzer,GPIO.HIGH)
                        GPIO.output(red_led,GPIO.HIGH)
                        time.sleep(0.2)
                        GPIO.output(buzzer,GPIO.LOW)
                        GPIO.output(red_led,GPIO.LOW)
                        time.sleep(0.2)
                    print("updating sheets")
                    sheetsupdate("-","-","-",rfid_tag_id,"Invalid Card")
                    GPIO.output(green_led,GPIO.LOW)
                    print("both false")
                

                if(tag_valid):
                    if(get_fingerprint()):
                        # cam.capture()
                        open_door()
                        print("FName: "+id[0])
                        print("LName: "+id[1])
                        print("ID: "+id[2])
                        sheetsupdate(id[0],id[1],id[2],rfid_tag_id,"Valid")
                    else:
                        oled.invalid_fing()
                        print("Invalid Fingerprint")
                        sheetsupdate(id[0],id[1],id[2],rfid_tag_id,"FP Invalid")

id=[]
try:
        main()


# Reset by pressing CTRL + C
except KeyboardInterrupt:
    print("Code stopped by User")
    cam.capture()
    print("Capture")
    GPIO.cleanup()
    print("GPIO Cleanup Called!!")
    cam.camera.close()
    print("Camera Closed")

except:
    print("Program Crashed")
    cam.capture()
    print("Capture")
    GPIO.cleanup()
    print("GPIO Cleanup Called!!")
    cam.camera.close()
    print("Camera Closed")
    

#####################MAIN_TRY_EXCEPT#####################
