import requests
import Adafruit_BMP.BMP085 as BMP085 # Imports the BMP library
import os
import glob
import time
from subprocess import PIPE, Popen
import subprocess
import sys
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
redPin = 33
greenPin = 35
bluePin = 37

headers = {
    'accept': 'application/json',
    'X-Api-Key': 'rGtkL4XOE0hhTqZf',
    'Content-Type': 'application/json',
}

while True:
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(greenPin, GPIO.OUT)
    GPIO.output(greenPin, GPIO.HIGH)
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(bluePin, GPIO.OUT)
    GPIO.output(bluePin, GPIO.HIGH)
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(redPin, GPIO.OUT)
    GPIO.output(redPin, GPIO.HIGH)
    #Dallas - Temp
    
    
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

teplotaDallas = str(read_temp())

teplota = '{ "value": '+teplotaDallas+'}'
    
    response = requests.post('https://api.nag-iot.zcu.cz/v2/value/dallas', headers=headers, data=teplota)
    
    
    #BMP180 - Teplota
    
    
    sensor = BMP085.BMP085()
    
    teplotaBMP = str(sensor.read_temperature())
    
    teplota2 = '{ "value": '+teplotaBMP+'}'
    
    response = requests.post('https://api.nag-iot.zcu.cz/v2/value/bmp', headers=headers, data=teplota2)
    
    
    #BMP - Tlak
    
    
    tlak = str(sensor.read_pressure())
    
    tlakBMP = '{ "value": '+tlak+'}'
    
    response = requests.post('https://api.nag-iot.zcu.cz/v2/value/tlak', headers=headers, data=tlakBMP)
    
    
    #BMP - Altitude
    
    
    altitude = str(sensor.read_altitude())
    
    altitudeBMP = '{ "value": '+altitude+'}'
    
    response = requests.post('https://api.nag-iot.zcu.cz/v2/value/vyska', headers=headers, data=altitudeBMP)
    
    
    #BMP - Sea tlak
    
    
    stlak = str(sensor.read_sealevel_pressure())
    
    stlakBMP = '{ "value": ' + stlak + '}'
    
    response = requests.post('https://api.nag-iot.zcu.cz/v2/value/stlak', headers=headers, data=stlakBMP)
    
    
    #CPU Temp
    
    
    def get_cpu_temperature():
        """get cpu temperature using vcgencmd"""
        process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE)
        output, _error = process.communicate()
        return float(output[output.index('=') + 1:output.rindex("'")])
    
    cputemp = str(get_cpu_temperature())
    
    cputempSYS = '{ "value": ' + cputemp + '}'
    
    response = requests.post('https://api.nag-iot.zcu.cz/v2/value/cputemp', headers=headers, data=cputempSYS)
    
    
    #Ping
    
    try:
        op = subprocess.check_output(["ping", "nag-iot.zcu.cz", "-c", "1"])
        restime = str(op[op.index("mdev = ") + 7: op.index("mdev = ") + 12])
        
        pingtime = '{ "value": ' + restime + '}'
        
        response = requests.post('https://api.nag-iot.zcu.cz/v2/value/ping', headers=headers, data=pingtime)
    
    except:
        time.sleep(0.01)

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(bluePin, GPIO.OUT)
    GPIO.output(bluePin, GPIO.LOW)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(redPin, GPIO.OUT)
GPIO.output(redPin, GPIO.LOW)
for x in range(30):
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(greenPin, GPIO.OUT)
    GPIO.output(greenPin, GPIO.HIGH)
    time.sleep(1)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(greenPin, GPIO.OUT)
    GPIO.output(greenPin, GPIO.LOW)
    time.sleep(1)
