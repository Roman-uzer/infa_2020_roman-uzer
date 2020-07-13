from graph import*

def moveSnake(xNew, yNew):
	global x, y
	for k in range(len(snake) - 1, 0 , -1):
		newCoord = coords(snake[k-1])
		moveObjectTo(snake[k], newCoord[0], newCoord[1])
	moveObjectTo(snake[0], xNew, yNew)
	x = xNew; y = yNew
def update():
	if dx or dy:
		moveSnake(x + dx*a, y + dy*a)
def KeyPressed(event):
	global dx, dy
	if event.keycode == VK_LEFT:
		dx = -1; dy = 0
	if event.keycode == VK_RIGHT:
		dx = 1; dy = 0
	if event.keycode == VK_UP:
		dx = 0; dy = -1
	if event.keycode == VK_DOWN:
		dx = 0; dy = 1

windowSize(400, 400)
brushColor("blue")
rectangle(0, 0, 400, 400)
x = 100; y = 100; dx = 0; dy = 0; N = 20; a = 10
snake = []
brushColor("yellow")
penColor("yellow")
for i in range(N):
	obj = rectangle(x + i*a, y, x + i*a + a, y + a)
	snake.append(obj)
	brushColor("green")
onKey(KeyPressed)
onTimer(update, 500)
run()