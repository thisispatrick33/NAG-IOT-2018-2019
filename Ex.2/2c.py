import time, sys
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)

redPin = GPIO.PWM(33, 100)  # channel=31 frequency=100Hz
greenPin = GPIO.PWM(35, 100)  # channel=31 frequency=100Hz
bluePin = GPIO.PWM(37, 100)  # channel=31 frequency=100Hz
redPin.start(0)
greenPin.start(0)
bluePin.start(0)

def blink(pin):
    for dc in range(0, 101, 5):
        pin.ChangeDutyCycle(dc)
        time.sleep(0.1)


def turnOff(pin):
    for dc in range(100, -1, -5):
        pin.ChangeDutyCycle(dc)
        time.sleep(0.1)


def redOn():
    blink(redPin)


def redOff():
    turnOff(redPin)


def greenOn():
    blink(greenPin)


def greenOff():
    turnOff(greenPin)


def blueOn():
    blink(bluePin)


def blueOff():
    turnOff(bluePin)


def yellowOn():
    blink(redPin)
    blink(greenPin)


def yellowOff():
    turnOff(redPin)
    turnOff(greenPin)


def cyanOn():
    blink(greenPin)
    blink(bluePin)


def cyanOff():
    turnOff(greenPin)
    turnOff(bluePin)


def magentaOn():
    blink(redPin)
    blink(bluePin)


def magentaOff():
    turnOff(redPin)
    turnOff(bluePin)


def whiteOn():
    blink(redPin)
    blink(greenPin)
    blink(bluePin)


def whiteOff():
    turnOff(redPin)
    turnOff(greenPin)
    turnOff(bluePin)


print("""Ensure the following GPIO connections: R-33, G-35, B-37
    Colors: Red, Green, Blue, Yellow, Cyan, Magenta, and White""")


def main():
    while True:
        cmd = raw_input()
        
        if cmd == "red on":
            redOn()
        elif cmd == "red off":
            redOff()
        elif cmd == "green on":
            greenOn()
        elif cmd == "green off":
            greenOff()
        elif cmd == "blue on":
            blueOn()
        elif cmd == "blue off":
            blueOff()
        elif cmd == "yellow on":
            yellowOn()
        elif cmd == "yellow off":
            yellowOff()
        elif cmd == "cyan on":
            cyanOn()
        elif cmd == "cyan off":
            cyanOff()
        elif cmd == "magenta on":
            magentaOn()
        elif cmd == "magenta off":
            magentaOff()
        elif cmd == "white on":
            whiteOn()
        elif cmd == "off":
            whiteOff()
        else:
            print("Nevhodny vyber")

return


main()
