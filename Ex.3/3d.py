from RPi import GPIO
from time import sleep
import os
import glob
import time
import gaugette.gpio
import gaugette.ssd1306
import gaugette.platform
import Adafruit_BMP.BMP085 as BMP085 # Imports the BMP library



#Rotary encoder


clk = 16
dt = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_UP)
counter = 1
clkLastState = GPIO.input(clk)


#Dallas


os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'


def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temp():
    lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c


#BMP180


sensor = BMP085.BMP085()


#DISPLAY


spi_bus = 0
spi_device = 0
gpio = gaugette.gpio.GPIO()
spi = gaugette.spi.SPI(spi_bus, spi_device)
RESET_PIN = 15 # WiringPi pin 15 is GPIO14.
DC_PIN = 16 # WiringPi pin 16 is GPIO15.

led = gaugette.ssd1306.SSD1306(gpio, spi, reset_pin=RESET_PIN, dc_pin=DC_PIN, rows=64, cols=128) # Change rows & cols values depending on your display dimensions.

led.begin()
led.clear_display()
led.display()
led.invert_display()
time.sleep(0.5)
led.normal_display()
time.sleep(0.5)


hodnota = (str)(read_temp())+" *C"
pristroj = "DALLAS"
velicina = "Teplota"

led.clear_display()
led.draw_text2(0, 0, str(pristroj), 2)
led.draw_text2(0, 20, str(velicina)+":", 2)
led.draw_text2(0, 50, str(hodnota), 2)
led.display()


def getConnection():
    hostname = "nag-iot.zcu.cz"
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
        return True
    else:
        return False

while True:
    clkState = GPIO.input(clk)
    if clkState != clkLastState:
        dtState = GPIO.input(dt)
        if dtState != clkState:
            counter += 1
        else:
            counter -= 1
        if counter > 8:
            counter = 1
        if counter < 1:
            counter = 8
        
        if counter == 1:
            pristroj = "DALLAS"
            velicina = "Teplota"
            hodnota = (str)(read_temp())+" *C"
        elif counter == 2:
            pristroj = "BMP180"
            velicina = "Tlak -more"
            hodnota = (str)(sensor.read_sealevel_pressure())+" Pa"
        elif counter == 3:
            pristroj = "BMP180"
            velicina = "Tlak -local"
            hodnota = (str)(sensor.read_pressure())+" Pa"
        elif counter == 4:
            pristroj = "BMP180"
            velicina = "Teplota"
            hodnota = (str)(sensor.read_temperature())+" *C"
        elif counter == 5:
            pristroj = "BMP180"
            velicina = "Altitude"
            hodnota = (str)((int)(sensor.read_altitude()))+" m.n.m"
        elif counter == 6:
            pristroj = "RPi"
            velicina = "Datum"
            hodnota = time.strftime("%d-%m-%Y")
        elif counter == 7:
            pristroj = "RPi"
            velicina = "Cas"
            hodnota = time.strftime("%H:%M")
        elif counter == 8:
            pristroj = "Spojenie so"
            velicina = "serverom"
            if getConnection():
                hodnota = "Connected"
            else:
                hodnota = "Connection failed"
        led.clear_display()
        led.draw_text2(0, 0, str(pristroj), 2)
        led.draw_text2(0, 20, str(velicina)+":", 2)
        led.draw_text2(0, 50, str(hodnota), 2)
        led.display()
clkLastState = clkState
