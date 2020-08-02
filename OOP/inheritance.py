from random import randint
class person:
	def __init__(self, com):
		self.number = id(self)
		if com:
			self.command = 'red'
		else:
			self.command = 'blue'		
class hero(person):
	def __init__(self, lvl, com):
		person.__init__(self, com)
		self.level = lvl
	def level_up(self):
		self.level += 1
class soldier(person):
	def follow_the_hero(self, hero):
			return hero.number, self.number

hero_blue = hero(1, 0)
hero_red = hero(1, 1)

red_command = []
blue_command = []
for i in range(100):
	if randint(0,1):
		red_command.append(soldier(1))
	else:
		blue_command.append(soldier(0))
print('Количество солдат в команде красных:', len(red_command))
print('Количество солдат в команде синих:', len(blue_command))
if len(red_command) > len(blue_command):
	hero_red.level_up()
	print('Уровень героя КРАСНЫХ повышен до', hero_red.level)
else:
	hero_blue.level_up()
	print('Уровень героя СИНИХ повышен до', hero_blue.level)
print(red_command[1].follow_the_hero(hero_red))
