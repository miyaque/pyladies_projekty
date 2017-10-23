import turtle

wn = turtle.Screen()
t = turtle.Turtle()
n = 5

for i in range(19):
    t.forward(i*n)
    t.left(90)

t.forward(n*19)



wn.exitonclick()