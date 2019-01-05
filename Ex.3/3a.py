import gaugette.ssd1306
import gaugette.platform
import gaugette.gpio
import RPi.GPIO as GPIO
import time
import sys

clk = 16
dt = 20
RESET_PIN = 15 # WiringPi pin 15 is GPIO14.
DC_PIN = 16 # WiringPi pin 16 is GPIO15.

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

spi_bus = 0
spi_device = 0
gpio = gaugette.gpio.GPIO()
spi = gaugette.spi.SPI(spi_bus, spi_device)

led = gaugette.ssd1306.SSD1306(gpio, spi, reset_pin=RESET_PIN, dc_pin=DC_PIN, rows=64, cols=128) # Change rows & cols values depending on your display dimensions.
led.begin()
led.clear_display()
led.display()
led.invert_display()
time.sleep(0.5)
led.normal_display()
time.sleep(0.5)

counter = 0
ticsToCount = 0
clkLastState = GPIO.input(clk)
led.clear_display()
led.draw_text2(10,30,str(counter),2)
led.display()

while True:
    clkState = GPIO.input(clk)
    dtState = GPIO.input(dt)
    if clkState != clkLastState:
        if dtState != clkState:
            ticsToCount += 1
        else:
            ticsToCount -= 1
        if ticsToCount == 2:
            ticsToCount = 0
            counter += 1
            led.clear_display()
            led.draw_text2(10,30,str(counter),2)
            led.display()
        if ticsToCount == -2:
            ticsToCount = 0
            counter -= 1
            led.clear_display()
            led.draw_text2(10,30,str(counter),2)
            led.display()
    clkLastState = clkState
