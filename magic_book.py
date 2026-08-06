import math
import board
import neopixel
from adafruit_pixel_framebuf import PixelFramebuffer

# Constants
DATA_PIN = board.D18
PIXEL_BRIGHTNESS = 1

pixels = neopixel.NeoPixel(
	DATA_PIN,
)
