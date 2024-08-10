from turtle import*

v = 10

t = Turtle()
t.color("blue")
t.shape("circle")
t.width(10)
t.pendown()
t.speed(v)

def draw(x,y):
    t.goto(x,y)

def move(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
def red():
    t.color("Red")

def white():
    t.color("White")    


def yellow():
    t.color("Yellow")

def size():
    str_a = input("Введіть розмір:  ")
    print(str_a)

def square():
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)

def abobus():
    t.forward(60)
    t.left(120)
    t.forward(60)
    t.left(120)
    t.forward(60)
    t.left(120)

def circle():
    t.circle(50)

def move_up():
    t.goto(t.xcor(), t.ycor() + 10)
def move_down():
    t.goto(t.xcor(),t.ycor() - 10)
def move_right():
    t.goto(t.xcor() + 10, t.ycor())
def move_left():
    t.goto(t.xcor() - 10, t.ycor())

t.ondrag(draw)

scr = t.getscreen()

scr.onscreenclick(move)
scr.listen()

scr.onkey(square,'h')
scr.listen

scr.onkey(circle,'l')
scr.listen

scr.onkey(abobus,'k')
scr.listen

scr.onkey(red,'r')
scr.listen
       
scr.onkey(yellow,'n')
scr.listen



scr.onkey(white,'p')
scr.listen

scr.onkey(size,'e')

def startfill():
    t.begin_fill()

scr.onkey(startfill,'q')
scr.listen

def endfill():
    t.end_fill()

scr.onkey(endfill,'t')
scr.listen

scr.onkey(move_up,'Up')
scr.onkey(move_left,'Left')
scr.onkey(move_right,'Right')
scr.onkey(move_down,'Down')
