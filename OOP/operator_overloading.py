class Snow:
	def __init__(self, number):
		self.number_of_snowflakes = number
	def __add__(self, number):
		self.number_of_snowflakes += number
	def __sub__(self, number):
		self.number_of_snowflakes -= number
	def __mul__(self, number):
		self.number_of_snowflakes *= number
	def __truediv__(self, number):
		self.number_of_snowflakes //= number
	def makeSnow(self, number_of_snowflakes_row):
		self.row = self.number_of_snowflakes//number_of_snowflakes_row
		self.remainder = self.number_of_snowflakes % number_of_snowflakes_row
		if self.remainder:
			for i in range(self.row):
				print('*' * number_of_snowflakes_row)
			print('*' * self.remainder)
		else:
			for i in range(self.row):
				print('*' * number_of_snowflakes_row)
	def rewrite(self, new_number):
		self.number_of_snowflakes = new_number
snow = Snow(200)
snow.makeSnow(11)
snow / 2
snow.makeSnow(11)
snow.rewrite(20)
snow.makeSnow(5)
