import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23
GPIO.setup(31, GPIO.OUT)  #LED to GPIO24

try:
    while True:
        button_state = GPIO.input(29)
        if button_state == False:
            GPIO.output(31, GPIO.HIGH)
            print('Button Pressed...')
            time.sleep(0.2)
                else:
                    GPIO.output(31, GPIO.LOW)
except:
    GPIO.cleanup()
