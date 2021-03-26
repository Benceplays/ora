from turtle import *

class Szamok:

    scr = Screen()
    t = Turtle()

    def egy(self):
        self.t.left(90)
        self.t.forward(200)
        self.t.left(135)
        self.t.forward(100)
        self.t.penup()
        self.t.home()
        self.t.pendown()

    def ketto(self):
        self.t.forward(100)
        self.t.backward(100)
        self.t.left(40)
        self.t.forward(100)
        for i in range(240):
            self.t.forward(0.8)
            self.t.left(0.8)

    def harom(self):
        self.t.penup()
        self.t.backward(75)
        self.t.pendown()
        self.t.forward(40)
        for j in range(180):
            self.t.forward(1)
            self.t.left(1)

        self.t.right(180)

        for k in range(180):
            self.t.forward(1)
            self.t.left(1)

        self.t.forward(40)

    def negy(self):
        self.t.penup()
        self.t.forward(50)
        self.t.pendown()
        self.t.left(90)
        self.t.forward(200)
        for h in range(3):
            self.t.backward(100)
            self.t.right(90)

    def ot(self):
        self.t.penup()
        self.t.left(90)
        self.t.forward(20)
        self.t.right(90)

    def __init__(self):
        self.t.speed(0)
        self.negy()

        self.scr.mainloop()

Szamok()