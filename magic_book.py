import math
from random import randint
import time
import board
import neopixel

#* Setup
# Constants
DATA_PIN = board.D18
PIXEL_BRIGHTNESS = 1
LED_COUNT = 60

pixels = neopixel.NeoPixel(
	DATA_PIN,
	LED_COUNT,
	brightness=PIXEL_BRIGHTNESS,
	auto_write=False,
	pixel_order=neopixel.GRB
)

#* Main loop
while True:
	pixel = randint(0, LED_COUNT-1)
	pixel_colour = (randint(0, 254), randint(0, 254), randint(0, 254))
	pixels[pixel] = pixel_colour
	pixels.fill((255, 255, 255))
	time.sleep(0.1)
	pixels.show()
	print(f"Changed pixel {pixel} to {pixel_colour}")
