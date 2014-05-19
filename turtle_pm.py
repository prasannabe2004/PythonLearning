import turtle               # allows us to use the turtles library


window = turtle.Screen()
window.bgcolor("red")

def draw_square(some):
	for i in range(0,4):
		some.forward(100)
		some.left(90)

def draw_circle():
	brad = turtle.Turtle()
	brad.circle(50)
	brad.color("green")
	brad.shape("arrow")

def draw_triangle(some):
	for i in range(0,3):
		some.forward(100)
		some.left(120)

def draw_art():
	art = turtle.Turtle()
	art.shape("turtle")
	art.speed(5)
	for i in range(1,37):
		draw_triangle(art)
		art.left(10)

#draw_square()
#draw_circle()
#draw_triangle()
draw_art()
window.exitonclick()


