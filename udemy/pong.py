from tkinter import *
import time
import random

tk = Tk()
tk.title("Pong!")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk,width=500,height=400,bd=0,highlightthickness=0)
canvas.config(bg='black')
canvas.pack()
tk.update()

canvas.create_line(250,0,250,400,fill='white')


class Ball:
    def __init__(self,canvas, paddle, color):
        self.canvas = canvas
        self.id= canvas.create_oval(10,10,25,25,fill=color)


ball = Ball(canvas,'orange')

while 1:
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
