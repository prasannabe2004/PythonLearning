import turtle               # allows us to use the turtles library


window = turtle.Screen()
window.bgcolor("white")

def draw_hex(some):
	for i in range(0,6):	
		some.forward(50)
		some.left(60)

def draw_art():
	art = turtle.Turtle()
	art.speed(20)
	art.color("red")
	art.shape("arrow")

	for i in range(1,19):
		draw_hex(art)
		art.left(20)

draw_art()
window.exitonclick()


