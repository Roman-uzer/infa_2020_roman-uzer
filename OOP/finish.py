from random import randint
class Data:
	def __init__(self, *info):
		self.info = list(info)
	def __getitem__(self, i):
		return self.info[i]
class Teacher:
	def teach(self, info, *pupil):
		for i in pupil:
			i.take(info)
class Pupil:
	def __init__(self):
		self.knowledge = []
	def take(self, info):
		self.knowledge.append(info)
	def forget(self):
		self.knowledge.pop(randint(0, len(self.knowledge) - 1))


lesson = Data('class', 'object', 'inheritance', 'polymorphism', 'encapsulation')
marIvanna = Teacher()
vasy = Pupil()
pety = Pupil()
marIvanna.teach(lesson[2], vasy, pety)
print(vasy.knowledge)
vasy.take(lesson[1])
print(vasy.knowledge)
vasy.forget()
print(vasy.knowledge)