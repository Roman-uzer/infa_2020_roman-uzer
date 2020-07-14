from graph import*
from math import*

#корабль

def ship(x1, y1, x2, y2):
	ship_list = []
	h = y2 - y1
	brushColor(0,0,0)
	penColor(0,0,0)
	pillar = rectangle(x1, y1, x2, y2)
	ship_list.append(pillar)
	penColor(150,150,150)
	brushColor(223,214,154)
	up_sail = polygon([(x2,y1), (h/6 + x2, h/2 + y1), 
			 (h/1.8 + x2, h/2 + y1), (x2, y1)])
	ship_list.append(up_sail)
	down_sail = polygon([(x2,y2), (h/6 + x2, h/2 + y1),
	    	 (h/1.8 + x2, h/2 + y1), (x2, y2)])
	ship_list.append(down_sail)
	penColor(220,79,100)
	brushColor(187,79,1)
	x11 = x1 - h/1.9
	x22 = h/1.17 + x2
	y22 = h/3.3 + y2
	body = rectangle(x11, y2, x22, y22)
	ship_list.append(body)
	nose = polygon([(x22, y2),(h/1.55 + x22, y2),
		     (x22, y22),(x22, y2)])
	ship_list.append(nose)
	r = y22 - y2
	til = arc(x11 - r, y2 - r, x11 + r, y22, 180, 270)
	ship_list.append(til)
	brushColor("black")
	penColor("black")
	window1 = circle(x2 + h, y2 + h/10, h/12.3)
	ship_list.append(window1)
	brushColor("white")
	window2 = circle(x2 + h, y2 + h/10, h/16.5)
	ship_list.append(window2)
	return ship_list
def move_ship(xNew, yNew):
	global x1,y1
	for i in range(len(obj)):
		coord_obj = coords(obj[i])
		moveObjectTo(obj[i], xNew + coord_obj[0] - x1, 
					 yNew + coord_obj[1] - y1)
	x1 = xNew; y1 = yNew
def move_mini_ship(xNew, yNew):
	global x1_mini_ship, y1_mini_ship
	for i in range(len(obj_mini_ship)):
		coord_obj = coords(obj_mini_ship[i])
		moveObjectTo(obj_mini_ship[i], xNew + coord_obj[0] - x1_mini_ship,
					 yNew + coord_obj[1] - y1_mini_ship)
	x1_mini_ship = xNew; y1_mini_ship = yNew
#облака
def clouds(x1,y1,x2,y2):
	brushColor(255,255,255)
	oval(x1,y1,x2,y2)
	r1 = (x2 - x1)/2
	r2 = (y2 - y1)/2
	oval(x1 + 1.5 * r1 , y1 ,
		 x2 + 1.5 * r1 , y2)
	oval(x1 - r1 , y1 + 0.9 * r2,
		 x2 - r1 , y2 + 0.9 * r2)
	oval(x1 + 0.6 * r1 , y1 + 1.2 * r2 ,
		 x2 + 0.6 * r1 , y2 + 1.2 * r2)
	oval(x1 + 2 * r1 , y1 + 1.2 * r2 ,
		 x2 + 2 * r1 , y2 + 1.2 * r2)
	oval(x1 + 3 * r1 , y1 ,
		 x2 + 3 * r1 , y2)
	oval(x1 + 3.5 * r1 , y1 + 1.2 * r2 ,
		 x2 + 3.5 * r1 , y2 + 1.2 * r2)
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
#Солнце
def f_sun(x, y):
	brushColor("yellow")
	penColor("yellow")
	sun = []
	f = 0
	fi = pi/50
	while f < 2 * pi:
		x1 = x + 45 * cos(f)
		y1 = y + 45 * sin(f)
		x2 = x + 1.3 * 45 * cos(fi)
		y2 = y + 1.3 * 45 * sin(fi)
		sun.append([x1,y1])
		sun.append([x2,y2])
		f += pi/25
		fi += pi/25
	return polygon(sun)
def move_sun(x1N, y1N):
	global x_sun, y_sun
	moveObjectTo(sun, x1N, y1N)
	x_sun = x1N; y_sun = y1N
#волны
def waves(x_waves):
	wavess = []
	brushColor(66, 30, 224)
	penColor(66, 30, 224)
	for i in range(8):
		ocean_waves = circle(x_waves, 250, 37)
		wavess.append(ocean_waves)
		x_waves += 86
	brushColor("yellow")
	penColor("yellow")
	x_beach = (x_waves - 86*8) - 42
	for i in range(8):
		beach_waves = circle(x_beach, 310, 37)
		wavess.append(beach_waves)
		x_beach += 86
	return wavess
def move_waves(xNew):
	global x_waves
	xN = xNew - xCoord(obj_waves[0])
	for i in range(len(obj_waves)):
		coords_waves = coords(obj_waves[i])
		x = coords_waves[0]
		y = coords_waves[1]
		moveObjectTo(obj_waves[i], x + xN, y)
	x_waves = xNew
def update_waves():
	global dx_waves
	if x_waves == 1 or x_waves == -30:
		dx_waves = -dx_waves
	move_waves(x_waves + dx_waves)
def update_sun():
	global dx_sun, dy_sun
	dx_sun = sin(fi); dy_sun = cos(fi)
	move_sun(x_sun + dx_sun, y_sun + dy_sun)
def update_ship():
	global dy, fi, coord_object, x1
	dy = sin(fi)
	if x1 >= 800:
		for i in range(len(obj)):
			coord_object = coords(obj[i])
			xN = coord_object[0] - 900; yN = coord_object[1]
			moveObjectTo(obj[i], xN, yN)
		x1 = xN
	fi += pi/3
	move_ship(x1 + dx,y1 + dy)
def update_mini_ship():
	global coords_object, x1_mini_ship
	if x1_mini_ship >= 700:
		for i in range(len(obj_mini_ship)):
			coord_object = coords(obj_mini_ship[i])
			xN = coord_object[0] - 800; yN = coord_object[1]
			moveObjectTo(obj_mini_ship[i], xN, yN)
		x1_mini_ship = xN
	move_mini_ship(x1_mini_ship + dx, y1_mini_ship + dy)

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
x_waves = - 5; dx_waves = 1
obj_waves = waves(x_waves)
penColor(100,100,100)
line(0,280,600,280)
x_sun = 560; y_sun = 70
sun = f_sun(x_sun, y_sun)
penColor(150,150,150)
clouds(120,30,150,60)
clouds(60,100,105,130)
penColor(130,130,130)
clouds(250,8,300,65)
x1_mini_ship = 205; y1_mini_ship = 155
x2_mini_ship = 207; y2_mini_ship = 190
obj_mini_ship = ship(x1_mini_ship, y1_mini_ship,
					 x2_mini_ship, y2_mini_ship)
x1 = 405; y1 = 110; x2 = 410; y2 = 210; dx = 1; fi = 0
obj = ship(x1,y1,x2,y2)
umbrella(90, 230, 96, 260, 70)
umbrella(203, 270, 204, 290, 25)

onTimer(update_sun, 50)
onTimer(update_ship, 50)
onTimer(update_mini_ship, 50)
onTimer(update_waves, 50)

run()