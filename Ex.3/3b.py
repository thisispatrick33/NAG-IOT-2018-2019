import Adafruit_BMP.BMP085 as BMP085 # Imports the BMP library
import time

sensor = BMP085.BMP085()

while True:
    print ('Altitude = {0:0.2f} m'.format(sensor.read_altitude()))
    print ('Sealevel Pressure = {0:0.2f}Pa'.format (sensor.read_sealevel_pressure()))
    time.sleep(1)
