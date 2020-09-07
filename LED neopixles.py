# this example is from adafruit
# https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/neopixels

"""This example lights up the first NeoPixel red."""
import time
from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.05
cp.pixels.fill((50,50,50))
 
i=0;
while True:
    cp.pixels[0] = (255-i, i, 0)
    cp.pixels[9] = (255-i, i, 0)
    cp.pixels[1] = (0,255-i, i, )
    cp.pixels[8] = (0,255-i, i, )
    cp.pixels[2] = (i, 0,255-i, )
    cp.pixels[7] = (i, 0,255-i, )
    i+=1
    if(i>255) :
        i=0
    time.sleep(0.01)
