import turtle
n = int(input('Zadejte jak velky domecek mam vykreslit: '))

wn = turtle.Screen()

t = turtle.Turtle()

t.left(90)
t.forward(n)
t.right(90)
t.forward(n)
t.right(135)
t.forward(n*2**0.5)
t.left(135)
t.forward(n)
t.left(90)
t.forward(n)
t.left(30)
t.forward(n)
t.left(120)
t.forward(n)
t.left(75)
t.forward(n*2**0.5)



wn.exitonclick()

