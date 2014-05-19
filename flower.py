import turtle               # allows us to use the turtles library


window = turtle.Screen()
window.bgcolor("blue")

def draw_circle(some):
	some.circle(50)

def draw_art():
	art = turtle.Turtle()
	art.speed(20)
	art.color("white")
	art.shape("arrow")
	for i in range(1,19):
		draw_circle(art)
		art.left(20)
	art.color("green")
	art.right(90)
	art.pensize(5)
	art.forward(200)

draw_art()
window.exitonclick()


