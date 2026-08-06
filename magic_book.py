import math
from random import randint
import time
import board
import neopixel

#* Setup
# Constants
DATA_PIN = board.D18
PIXEL_BRIGHTNESS = 0.5
LED_COUNT = 60

pixels = neopixel.NeoPixel(
	DATA_PIN,
	LED_COUNT,
	brightness=PIXEL_BRIGHTNESS,
	auto_write=False,
	pixel_order=neopixel.GRB
)

#* Main loop
pixels.fill((0, 0, 0))
pixels.show()
time.sleep(2)
while True:
	pixel = randint(0, LED_COUNT-1)
	pixel_colour = (randint(0, 254), randint(0, 254), randint(0, 254))
	pixels[pixel] = pixel_colour
	pixels.show()
	# time.sleep(0.1)
	print(f"Changed pixel {pixel} to {pixel_colour}")
