
from turtle import *
from random import *
from time import *

t = Turtle()
t.color("blue")
t.shape("turtle")
t.penup()
t.speed(3)
t2 = Turtle()
t2.color("blue")
t2.shape("turtle")
t2.penup()
t2.goto(-90, 200)
t2.write("ГРА ВПІЙМАЙ ЧЕРЕПАШКУ ", font=("Arial", 12, "bold"))
t2.goto(-90, 300)
def catch(x, y):
    x = randint(-200, 200)
    y = randint(-200, 160)
    t.write("AI", font=("Arial", 12, "bold"))
    t.moved = 1
    t.goto(x, y)
    
    t.p = t.p + 1
    

    



t.p = 0
t.moved = 0
t.onclick(catch)


while t.p < 3:
    x = randint(-200, 200)
    y = randint(-200, 160)
    
    if t.moved == 0:
        t.goto(x, y)
    t.moved = 0
    sleep(0.5)

t.hideturtle()
if t.p >= 3:
    t2.goto(-70, 180)
    t2.color("green")
    t2.write("ти", font=("Arial", 12, "bold"))



  
    t2.goto(-45, 180) 
    t2.write("спіймав ", font=("Arial", 12, "bold"))

   
  
    t2.goto(26, 180)
    t2.write("черепашку!", font=("Arial", 12, "bold"))
t2.goto(-90, 300)

  
