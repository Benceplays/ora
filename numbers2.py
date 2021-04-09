from turtle import *
from datetime import *
from j_clock import *
class Numbers2:
    scr = Screen()
    clk = Clock(scr)
    t = Turtle()

    def reset(self):
        self.t.penup()
        self.t.home()
        self.t.pendown()

    def zold(self):
        self.t.begin_fill()
        self.t.fillcolor("Lime")

        self.t.forward(100)
        self.t.left(45)
        self.t.forward(25)
        self.t.left(90)
        self.t.forward(25)
        self.t.left(45)
        self.t.forward(100)
        self.t.left(45)
        self.t.forward(25)
        self.t.left(90)
        self.t.forward(25)

        self.t.end_fill()

    def sotet(self):
        self.t.begin_fill()
        self.t.fillcolor(0, 0.05, 0)

        self.t.forward(100)
        self.t.left(45)
        self.t.forward(25)
        self.t.left(90)
        self.t.forward(25)
        self.t.left(45)
        self.t.forward(100)
        self.t.left(45)
        self.t.forward(25)
        self.t.left(90)
        self.t.forward(25)

        self.t.end_fill()

    def egy(self):
        self.sotet()
        self.t.back(25)
        self.t.right(225)
        self.t.penup()
        self.t.forward(25)
        self.t.pendown()
        self.sotet()
        self.t.penup()
        self.t.back(25)
        self.t.right(135)
        self.t.forward(50)
        self.t.right(90)
        self.t.forward(25)
        self.t.left(90)
        self.t.right(90)
        self.t.forward(25)
        self.t.pendown()
        self.zold()
        self.t.penup()
        self.t.forward(133)
        self.zold()
        self.t.penup()
        self.t.forward(170)
        self.t.right(90)
        self.t.forward(17.5)
        self.t.left(90)
        self.t.pendown()
        self.zold()
        self.t.penup()
        self.t.forward(125)
        self.t.right(90)
        self.t.forward(33)
        self.t.pendown()
        self.sotet()
        self.t.penup()
        self.t.forward(134.5)
        self.t.right(90)
        self.t.forward(30)
        self.t.pendown()
        self.sotet()
        self.reset()

    def ketto(self):
        self.szam1()
        self.t.left(90)
        self.t.penup()
        self.t.forward(25)
        self.t.pendown()
        self.szam2()
        self.t.penup()
        self.t.forward(125)
        self.t.right(90)
        self.t.forward(35)
        self.t.pendown()
        self.szam3()
        self.t.penup()
        self.t.forward(133)
        self.t.right(90)
        self.t.forward(25)
        self.t.pendown()
        self.szam4()
        self.t.penup()
        self.t.forward(170)
        self.t.right(90)
        self.t.forward(17.5)
        self.t.left(90)
        self.t.pendown()
        self.szam5()
        self.t.penup()
        self.t.forward(125)
        self.t.right(90)
        self.t.forward(33)
        self.t.pendown()
        self.szam6()
        self.t.penup()
        self.t.forward(134.5)
        self.t.right(90)
        self.t.forward(30)
        self.t.pendown()
        self.szam7()
        self.reset()

    def __init__(self):
        self.egy()

Numbers2()