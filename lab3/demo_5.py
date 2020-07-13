from graph import*
q = -5
def update():
	global q
	if xCoord(obj2) >= 380:
		q = -q
	if xCoord(obj2) <= 0:
		q=-q
	moveObjectBy(obj2, q, 0)

def downdate():
	if  direction == True:
		moveObjectBy(obj, - 5, 0)
	else:
		moveObjectBy(obj, 5, 0)


def keyPressed(event):
	if event.keycode == VK_ESCAPE:
		close()

windowSize(400, 400)
brushColor("blue")
rectangle(0, 0, 400, 400)
x = 380 
y = 100
penColor("yellow")
brushColor("yellow")
obj = rectangle(x, y, x + 20, y + 20)
x -= 380
y -= 40
obj2 = rectangle(x, y, x + 20, y + 20)


onTimer(update, 50)
onKey(keyPressed)
run()