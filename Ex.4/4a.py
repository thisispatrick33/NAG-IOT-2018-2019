import requests
import Adafruit_BMP.BMP085 as BMP085 # Imports the BMP library
import time

headers = {
    'accept': 'application/json',
    'X-Api-Key': 'rGtkL4XOE0hhTqZf',
    'Content-Type': 'application/json',
}

sensor = BMP085.BMP085()

teplota = str(sensor.read_temperature())
print(teplota)

data = '{ "value": '+teplota+'}'

response = requests.post('https://api.nag-iot.zcu.cz/v2/value/bmp', headers=headers, data=data)
