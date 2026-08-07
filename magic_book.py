import math
from random import randint
import time
import board
import neopixel
from LED import *
from helper_functions import *

#* Setup
# Constants
DATA_PIN = board.D12
PIXEL_BRIGHTNESS = 1
LED_COUNT = 60

powering_up_progress = 0
powering_up_delay = 0.05

power_up_complete = False

idle_time = 3
idling_progress = 0
idling_delay = 0.05

casting_complete = False

# Connect LEDs to custom data structure
pixels = neopixel.NeoPixel(
	DATA_PIN,
	LED_COUNT,
	brightness=PIXEL_BRIGHTNESS,
	auto_write=False,
	pixel_order=neopixel.GRB
)

leds = []
for i in range(LED_COUNT):
	leds.append(LED(i, pixels[i]))

#* Main loop
# Debug light-up
pixels.fill((255, 255, 255))
pixels.show()
time.sleep(1)

pixels.fill((0, 0, 0))
pixels.show()
time.sleep(2)

# Show powering up animation
print("Powering up...")
while powering_up_progress < LED_COUNT:
	# Update LED colour
	for i in range(powering_up_progress):
		colour = leds[i].step_power_up()
		pixels[i] = colour

	pixels.show()
	print_leds(leds)

	powering_up_progress += 1
	time.sleep(powering_up_delay)

print("Powered up!")
# Show power up finish animation
while not power_up_complete:
	power_up_complete = True

print("Waiting for spell...")
# Show idling animation
while idling_progress <= idle_time:
	# Update LED colour
	for led in leds:
		led.step_idle()

	pixels.show()

	idling_progress += idling_delay

print("Casting spell...")
# Show spell-casting animation
while not casting_complete:
	casting_complete = True

print("Spell casted!")

print("Idling...")
while True:
	for led in leds:
		led.step_idle()

	pixels.show()
