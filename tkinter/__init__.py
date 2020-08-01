class person:
	def __init__(self, n, s, sk = 1):
		self.name = n
		self.surname = s
		self.skill = sk
	def infomation(self):
		print(self.name, self.surname, self.skill)
	def __del__(self):
		print('До свидания, мистер', self.surname, self.name, '!')
sasha = person('alex', 'shiryaev')
lesha = person('alexei', 'ardatov', 10)
roman = person('roman', 'melnikov', 9999999)
sasha.infomation()
lesha.infomation()
roman.infomation()
x = input('Кого будем увольнять? Напишите цифру:  ')
if int(x) == 1:
	del sasha
input()