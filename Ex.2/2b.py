import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(31, GPIO.OUT)

p = GPIO.PWM(31, 100)  # channel=31 frequency=100Hz
p.start(0)
try:
    while True:
        print("work")
        for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
                for dc in range(100, -1, -5):
                    p.ChangeDutyCycle(dc)
                    time.sleep(0.1)
except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()
