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
	for i in range(10):
		pixels[i] = (0, 0, 0)

	for i in range(10, 20):
		pixels[i] = (1, 1, 1)

	for i in range(20, 30):
		pixels[i] = (5, 5, 5)

	for i in range(30, 40):
		pixels[i] = (10, 10, 10)

	for i in range(40, 50):
		pixels[i] = (20, 20, 20)

	for i in range(50, 60):
		pixels[i] = (255, 255, 255)

	pixels.show()
