class addition:
	def __init__(self, n):
		self.number = n
	def __add__(self, obj):
		return self.number - obj.number

five = addition(5)
nine = addition(9)

print(five + nine)