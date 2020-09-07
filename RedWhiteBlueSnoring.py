# Carl Ferkinhoff
# starting from from adafruit example
# https://learn.adafruit.com/welcome-to-circuitpython/creating-and-editing-code
#
import time
from adafruit_circuitplayground import cp

# set up the (red) LED
#cp.pixels.brightness = 0.1
#cp.pixels.fill((50,50,50))
 

while True:
    length = 255 #sets the length of the snore
    j=0
    wait_down = .01
    wait_up = .01
    while (j<length):
        cp.pixels[0]=(255-j, 0, 0)
        cp.pixels[9]=(255-j, 0, 0)
        cp.pixels[1]=(0, 0,255-j)
        cp.pixels[8]=(0, 0,255-j)
        cp.pixels[2]=(255-j,255-j,255-j)
        cp.pixels[7]=(255-j,255-j,255-j)
        cp.pixels[3]=(0, 0,255-j)
        cp.pixels[6]=(0, 0,255-j)
        cp.pixels[4]=(255-j, 0, 0)
        cp.pixels[5]=(255-j, 0, 0)
        j = j+1
        time.sleep(wait_down)
    time.sleep(.01)
    while (j>0):
        cp.pixels[0]=(255-j, 0, 0)
        cp.pixels[9]=(255-j, 0, 0)
        cp.pixels[1]=(0, 0,255-j)
        cp.pixels[8]=(0, 0,255-j)
        cp.pixels[2]=(255-j,255-j,255-j)
        cp.pixels[7]=(255-j,255-j,255-j)
        cp.pixels[3]=(0, 0,255-j)
        cp.pixels[6]=(0, 0,255-j)
        cp.pixels[4]=(255-j, 0, 0)
        cp.pixels[5]=(255-j, 0, 0)
        j = j-1
        time.sleep(wait_up)
