# print("Vtom vnuk křik': \"Hleď!\"")
# print('"Jen ho nech," řek\' děd. "Kdo zná líp kraj?"')
#
# print('--\N{LATIN SMALL LETTER L WITH STROKE}--')
# print('--\N{SECTION SIGN}--')
# print('--\N{PER MILLE SIGN}--')
# print('--\N{BLACK STAR}--')
# print('--\N{SNOWMAN}--')
# print('--\N{KATAKANA LETTER TU}--')
#
# print('C:\\PyLadies\\Nový adresář')
#
# basen = '''Haló haló!
# Co se stalo?
# Prase kozu potrkalo!'''
# print(basen)
#
#
#
# vypis = '{}×{} je {}'.format(3, 4, 3 * 4)
# print(vypis)

import turtle
n = 50#int(input('Zadejte jak velky domecek mam vykreslit: '))

wn = turtle.Screen()

t = turtle.Turtle()


for i in range(3):
    t.left(90)
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

