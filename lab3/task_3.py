from graph import*
from math import*

windowSize(600,402)
canvasSize(600,402)
#фон
penColor(162,245,255)
brushColor(162,245,255)
rectangle(0,0,600,186)

brushColor(66,30,224)
penColor(66,30,224)
rectangle(0,186,600,280)

brushColor("yellow")
penColor("yellow")
rectangle(0,280,600,402)
#волны
def blue_circle():
	brushColor(66,30,224)
	penColor(66,30,224)
	x = 64
	for i in range(7):
		circle(x,250,37)
		x += 86

def yellow_circle():
	brushColor("yellow")
	penColor("yellow")
	x = 21
	for i in range(7):
		circle(x,310,37)
		x += 86
blue_circle()
yellow_circle()
penColor(100,100,100)
line(0,280,600,280)
#Солнце
brushColor("yellow")
penColor("yellow")
sun = []
f = 0
fi = pi/50
while f < 2 * pi:
	x1 = 515 + 45 * cos(f)
	y1 = 70 + 45 * sin(f)
	x2 = 515 + 57 * cos(fi)
	y2 = 70 + 57 * sin(fi)
	sun.append([x1,y1])
	sun.append([x2,y2])
	f += pi/25
	fi += pi/25
polygon(sun)
#облака
def clouds(x1,y1,x2,y2):
	brushColor(255,255,255)
	oval(x1,y1,x2,y2)
	r1 = (x2 - x1)/2
	r2 = (y2 - y1)/2
	oval(x1 + 1.5 * r1 , y1 , x2 + 1.5 * r1 , y2)
	oval(x1 - r1 , y1 + 0.9 * r2, x2 - r1 , y2 + 0.9 * r2)
	oval(x1 + 0.6 * r1 , y1 + 1.2 * r2 , x2 + 0.6 * r1 , y2 + 1.2 * r2)
	oval(x1 + 2 * r1 , y1 + 1.2 * r2 , x2 + 2 * r1 , y2 + 1.2 * r2)
	oval(x1 + 3 * r1 , y1 , x2 + 3 * r1 , y2)
	oval(x1 + 3.5 * r1 , y1 + 1.2 * r2 , x2 + 3.5 * r1 , y2 + 1.2 * r2)
penColor(150,150,150)
clouds(120,30,150,60)
clouds(60,100,105,130)
penColor(130,130,130)
clouds(250,8,300,65)
#зонтик
def umbrella(x1,y1,x2,y2,h):
	penColor(228,131,18)
	brushColor(228,131,18)
	rectangle(x1,y2,x2,((y2 - y1) * 4) + y2)

	brushColor(244,80,80)
	penColor(221,73,99)
	rectangle(x1,y1,x2,y2)
	polygon([(x1,y1),(x1,y2),
		     (x1 - h,y2),(x1,y1)])
	polygon([(x2,y1),(x2,y2),
			 (x2 + h,y2),(x2,y1)])

	penColor(180,50,60)
	x = x1 - h/5
	for i in range(3):
		line(x1,y1,x,y2)
		x -= h/4
	x = x2 + h/5
	for i in range(3):
		line(x2,y1,x,y2)
		x += h/4
umbrella(90, 230, 96, 260, 70)
umbrella(203, 270, 204, 290, 25)
#корабль
def ship(x1, y1, x2, y2):
	h = y2 - y1
	brushColor(0,0,0)
	penColor(0,0,0)
	rectangle(x1, y1, x2, y2)
	penColor(150,150,150)
	brushColor(223,214,154)
	polygon([(x2,y1), (h/6 + x2, h/2 + y1), 
			 (h/1.8 + x2, h/2 + y1), (x2, y1)])
	polygon([(x2,y2), (h/6 + x2, h/2 + y1),
	    	 (h/1.8 + x2, h/2 + y1), (x2, y2)])

	penColor(220,79,100)
	brushColor(187,79,1)
	x11 = x1 - h/1.9
	x22 = h/1.17 + x2
	y22 = h/3.3 + y2
	rectangle(x11, y2, x22, y22)
	polygon([(x22, y2),(h/1.55 + x22, y2),
		     (x22, y22),(x22, y2)])
	r = y22 - y2
	arc(x11 - r, y2 - r, x11 + r, y22, 180, 270)

	brushColor("black")
	penColor("black")
	circle(x2 + h, y2 + h/10, h/12.3)
	brushColor("white")
	circle(x2 + h, y2 + h/10, h/16.5)

ship(405, 110, 410, 210)
ship(205, 155, 207, 190)

run()