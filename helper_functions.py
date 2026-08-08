def print_leds(leds) -> None:
	led_colours = []
	for led in leds:
		led_colours.append(led.colour)

	print("")

	for i in range(6):
		for j in range(10):
			if j != 9:
				print(led_colours[(i * 10) + j], end="")
			else:
				print(led_colours[(i * 10) + j])

	print("")
