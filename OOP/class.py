from random import randint
class warrior():
	health = 100

unit_1 = warrior()

unit_2 = warrior()
while unit_1.health and unit_2.health:
	input()
	random = randint(0,1)
	if random:
		unit_1.health -= 20
		print('Атаковал Юнит №2. У Юнита №1 осталось ', unit_1.health, 'hp')
	else:
		unit_2.health -= 20
		print('Атаковал Юнит №1. У Юнита №2 осталось ', unit_2.health, 'hp')
if unit_2.health:
	print('Юнит №2 одержал победу!!!')
else:
	print('Юнит №1 одержал победу!!!')
