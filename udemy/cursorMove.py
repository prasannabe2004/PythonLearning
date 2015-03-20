from tkinter import *

import time

tk = Tk()

canvas = Canvas(tk,width=500,height=500)

canvas.pack()

canvas.create_polygon(10,10,10,60,50,35)


def move():
    for i in range(1,51):
        canvas.move(1,5,0)
        tk.update()
        time.sleep(0.2)
    
def moveTriangle(event):
    if(event.keysym == 'Up'):
        canvas.move(1,0,-3)
    elif(event.keysym == 'Down'):
        canvas.move(1,0,3)
    elif(event.keysym == 'Left'):
        canvas.move(1,-3,0)
    elif(event.keysym == 'Right'):
        canvas.move(1,3,0)

canvas.bind_all('<KeyPress-Up>',moveTriangle)
canvas.bind_all('<KeyPress-Down>',moveTriangle)
canvas.bind_all('<KeyPress-Left>',moveTriangle)
canvas.bind_all('<KeyPress-Right>',moveTriangle)

