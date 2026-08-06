class LED:
	colour_delta = (0, 0, 25)
	start_colour = (0, 0, 0)
	end_colour = (0, 0, 255)

	def __init__(self, pixel_num: int, pixel):
		self.num = pixel_num
		self.pixel = pixel
		self.direction = 1
		self.colour = self.start_colour

	def step_power_up(self):
		"""
		Changes the LED's colour of a powering up animation by one step. Doesn't update the physical LED's colour, only the stored variable.
		"""
		# Increase colour
		if self.direction == 1:
			self.colour += self.colour_delta
		else:
			self.colour -= self.colour_delta

		# Change direction if needed
		if self.colour >= self.end_colour:
			if self.direction == 1:
				self.direction = -1
			else:
				self.direction = 1

	def step_idle(self):
		"""
		Changes the LED's colour of a pulsing animation by one step. Doesn't update the physical LED's colour, only the stored variable.
		"""
		pass

	def show(self):
		"""
		Updates the physical LED with the set colour and displays it.
		"""
		self.pixel = self.colour
		self.pixel.show()
