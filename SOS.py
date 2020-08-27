Austin Beyer's SOS code
# from adafruit
# https://learn.adafruit.com/welcome-to-circuitpython/creating-and-editing-code
#
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

while True:
  # note the new line: "a" is a variable that takes the values that are 
  # listed in square brackets.  This loop is sometimes called a "foreach"
  a=0.01
  for a in [1,2,3]:
        print("Hello, CircuitPython!")
        print(a)
        led.value = True
        time.sleep(a/8)
        led.value = False
        time.sleep(a/10)
  for a in [1,2,3]:
        print("Hello, CircuitPython!")
        print(a)
        led.value = True
        time.sleep(a/1)
        led.value = False
        time.sleep(a/2)
  for a in [1,2,3]:
        print("Hello, CircuitPython!")
        print(a)
        led.value = True
        time.sleep(a/8)
        led.value = False
        time.sleep(a/10)
