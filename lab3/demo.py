from graph import*

def update():
	global dx
	global dy
	if xCoord(obj) >= 380 or xCoord(obj) == 0:
		dx = -dx
	if yCoord(obj) >= 380 or yCoord(obj) == 0:
		dy = -dy 
	moveObjectBy(obj, dx, dy)
def keyPressed(event):
	global dx
	global dy
	if event.keycode == VK_ESCAPE:
		close()
	elif event.keycode == VK_LEFT:
		dx = -5; dy = 0
	elif event.keycode == VK_RIGHT:
		dx = 5; dy = 0
	elif event.keycode == VK_DOWN:
		dy = 5; dx = 5
	elif event.keycode == VK_UP:
		dy = -5; dx = - 5
	
	if xCoord(obj) >= 380 or xCoord(obj) <= 0:
		close()

windowSize(400, 400)
brushColor("blue")
rectangle(0, 0, 400, 400)
x = 100 
y = 100
dx = 5
dy = 0
penColor("yellow")
brushColor("yellow")
obj = rectangle(x, y, x + 20, y + 20)

onKey(keyPressed)
onTimer(update, 50)
run()