import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(31, GPIO.OUT)

while True:
    GPIO.output(31, GPIO.HIGH)
