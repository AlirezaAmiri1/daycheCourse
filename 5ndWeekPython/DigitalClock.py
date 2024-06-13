import time
import datetime as dte
import turtle

t1 = turtle.Turtle()
t2 = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("White")

secs = dte.datetime.now().second
mins = dte.datetime.now().minute
hrs = dte.datetime.now().hour
t2.pensize(2)
t2.color('Blue')
t2.penup()

t2.goto(-4, -4)
t2.pendown()

for j in range(2):
   t2.forward(190)
   t2.left(90)
   t2.forward(70)
   t2.left(90)
t2.hideturtle()

while True:
    t1.hideturtle()
    t1.clear()

    t1.write(str(hrs).zfill(2)
              + ":" + str(mins).zfill(2) + ":"
              + str(secs).zfill(2),
              font=("Callibri Narrow", 32, "bold"))
    time.sleep(1)
    secs += 1
    if secs == 60:
        secs = 0
        mins += 1
    if mins == 60:
        mins = 0
        hrs += 1
    if hrs == 13:
        hrs = 1