from graph import*

windowSize(600,402)
canvasSize(600,402)
penColor(162,245,255)
brushColor(162,245,255)
rectangle(0,0,600,186)
brushColor(66,30,224)
penColor(66,30,224)
rectangle(0,186,600,280)
brushColor("yellow")
penColor("yellow")
rectangle(0,280,600,402)
circle(530,60,40)
def cloud(x,y):
	penColor(150,150,150)
	brushColor(255,255,255)
	circle(x,y,15)
cloud(110,45)
cloud(135,45)
x = 95
for i in range(3):
	cloud(x,60)
	x += 25
cloud(160, 45)
cloud(170, 60)
penColor(221,73,99)
brushColor(244,80,80)
rectangle(80,260,85,230)
penColor(228,131,18)
brushColor(228,131,18)
rectangle(80,260,85,380)
def right_triangle(x,y,z):
	brushColor(244,80,80)
	penColor(221,73,99)
	polygon([(x,y),(x,y-30),
		     (z,y),(x,y)])
right_triangle(85,260,145)
right_triangle(80,260,20)
penColor(180,50,60)
x=85+60/4
for i in range(3):
	line(85,230,x,260)
	x+=60/4
x=80-60/4
for i in range(3):
	line(80,230,x,260)
	x-=60/4
brushColor(0,0,0)
penColor(0,0,0)
rectangle(405,210,410,110)

def triangle(x,y,z):
	penColor(150,150,150)
	brushColor(223,214,154)
	polygon([(x,y),(x-15,z),
		     (x+40,y),(x,y)])
triangle(425,160,110)
triangle(425,160,210)
penColor(220,79,100)
brushColor(187,79,1)
rectangle(350,210,500,240)
polygon([(500,210),(560,210),
	     (500,240),(500,210)])
brushColor("black")
penColor("black")
circle(514,220,8)
brushColor("white")
circle(514,220,6)
penColor(220,79,100)
brushColor(187,79,1)

x0 = 350
y0 = 210
arcs = [(x0,y0)]
x = 0
while x <= 30:
	y = (900 - x**2)**(1/2)
	xe = x0 - x
	ye = y0 + y
	point(xe,ye)
	arcs.append((xe,ye))
	x += 1
arcs.append((x0,y0))
polygon(arcs)

run()
