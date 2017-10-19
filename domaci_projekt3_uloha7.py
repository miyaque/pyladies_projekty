import turtle

wn = turtle.Screen()
t = turtle.Turtle()

n = int(input('Zadejte pocet stran: '))
uhel = 360/n

for i in range(n):
    t.forward(50)
    t.left(uhel)


wn.exitonclick()