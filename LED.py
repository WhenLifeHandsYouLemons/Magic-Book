class LED:
	colour_delta = [0, 0, 25]
	start_colour = [0, 0, 0]
	end_colour = [0, 0, 255]

	def __init__(self, pixel_num: int, pixel):
		self.num = pixel_num
		self.pixel = pixel
		self.direction = 1
		self.colour = self.start_colour

	def step_power_up(self) -> list:
		"""
		Changes the LED's colour of a powering up animation by one step. Doesn't update the physical LED's colour, only the stored variable.
		"""
		# Increase colour
		if self.direction == 1:
			self.colour[0] += self.colour_delta[0]
			self.colour[1] += self.colour_delta[1]
			self.colour[2] += self.colour_delta[2]
		else:
			self.colour[0] += self.colour_delta[0]
			self.colour[1] += self.colour_delta[1]
			self.colour[2] += self.colour_delta[2]

		# Change direction if needed
		if self.colour >= self.end_colour:
			if self.direction == 1:
				self.direction = -1
			else:
				self.direction = 1

		print(self.colour)
		return self.clamp_colour(self.colour)

	def step_idle(self) -> list:
		"""
		Changes the LED's colour of a pulsing animation by one step. Doesn't update the physical LED's colour, only the stored variable.
		"""
		return []

	def clamp_colour(self, colour: list) -> list:
		"""
		Clamps the components of the colour to be between [0, 255] inclusive.
		"""
		colour[0] = min(max(colour[0], 0), 255)
		colour[1] = min(max(colour[1], 0), 255)
		colour[2] = min(max(colour[2], 0), 255)

		return colour
