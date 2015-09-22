import turtle

t = turtle.Pen()

t.reset()

t.color(0,0,1)
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

t.left(90)
t.begin_fill()
t.circle(50)
t.end_fill()



turtle.mainloop()