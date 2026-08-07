import time
import board
import neopixel

DATA_PIN = board.D12
PIXEL_BRIGHTNESS = 1
LED_COUNT = 60

pixels = neopixel.NeoPixel(
	DATA_PIN,
	LED_COUNT,
	brightness=PIXEL_BRIGHTNESS,
	auto_write=False,
	pixel_order=neopixel.GRB
)

while True:
	print("On!")

	pixels.fill((255, 255, 255))
	pixels.show()
	time.sleep(1)

	print("Off!")

	pixels.fill((0, 0, 0))
	pixels.show()
	time.sleep(1)
