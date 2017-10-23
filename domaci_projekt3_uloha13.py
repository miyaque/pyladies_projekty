import turtle

wn = turtle.Screen()
t = turtle.Turtle()



n = 50

def house():
    for i in range(2):
        t.pendown()
        t.forward(n)
        t.right(90)
        t.forward(4/3*n)
        t.right(90)
    t.left(60)
    t.forward(n)
    t.right(120)
    t.forward(n)
    t.left(60)
    t.penup()



for i in range (2):
    for j in range(2):
        j *= -1
        i *= -1
        t.goto(j*(100), i*(-200))
        house()



wn.exitonclick()