import os
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import time




###############################OLED_INIT###############################
i2c = busio.I2C(3, 2)
disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
disp.fill(0)
disp.show()
width = disp.width
height = disp.height
image = Image.new("1", (width, height))
draw = ImageDraw.Draw(image)
draw.rectangle((0, 0, width, height), outline=0, fill=0)
padding = -2
top = padding
bottom = height - padding
x = 0
font = ImageFont.load_default()
draw.text((x, top + 0), "      TEAM LAZR", font=font, fill=255)
disp.show()
###############################OLED_INIT###############################


def home():
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    draw.text((x, top + 0), "      TEAM LAZR", font=font, fill=255)
    draw.text((x, top + 8), "Place your Card On", font=font, fill=255)
    draw.text((x, top + 16), " the RFID Scanner", font=font, fill=255)
    disp.image(image)
    disp.show()


def welc(fname,lname,sid):
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    draw.text((x, top + 0), "      TEAM LAZR", font=font, fill=255)
    draw.text((x, top + 8), "FName: "+fname, font=font, fill=255)
    draw.text((x, top + 16), "LName: "+lname, font=font, fill=255)
    draw.text((x, top + 25), "SID : "+sid, font=font, fill=255)
    disp.image(image)
    disp.show()

    time.sleep(1)

    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    draw.text((x, top + 0), "      TEAM LAZR", font=font, fill=255)
    draw.text((x, top + 8), "FName: "+fname, font=font, fill=255)
    draw.text((x, top + 16), "LName: "+lname, font=font, fill=255)
    draw.text((x, top + 25), "Scan Fingerprint", font=font, fill=255)
    disp.image(image)
    disp.show()


def invalid_card():
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    draw.text((x, top + 0), "      TEAM LAZR", font=font, fill=255)
    draw.text((x, top + 8), "Invalid Card", font=font, fill=255)
    draw.text((x, top + 16), " ", font=font, fill=255)
    draw.text((x, top + 25), "      !!Try Again!!", font=font, fill=255)
    disp.image(image)
    disp.show()


def invalid_fing():
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    draw.text((x, top + 0), "      TEAM LAZR", font=font, fill=255)
    draw.text((x, top + 8), "Invalid", font=font, fill=255)
    draw.text((x, top + 16), "FingerPrint", font=font, fill=255)
    draw.text((x, top + 25), "      !!Try Again!!", font=font, fill=255)
    disp.image(image)
    disp.show()

def intruder():
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    draw.text((x, top + 0), "      TEAM LAZR", font=font, fill=255)
    draw.text((x, top + 8), "!!Intruder Alert!!", font=font, fill=255)
    draw.text((x, top + 16), "", font=font, fill=255)
    draw.text((x, top + 25), "!!Intruder Alert!!", font=font, fill=255)
    disp.image(image)
    disp.show()


def buzzout():
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    draw.text((x, top + 0), "      TEAM LAZR", font=font, fill=255)
    draw.text((x, top + 8), "Buzzout", font=font, fill=255)
    draw.text((x, top + 16), " ", font=font, fill=255)
    draw.text((x, top + 25), " ", font=font, fill=255)
    disp.image(image)
    disp.show()
