x = int(input('První číslo: '))
y = int(input('Druhé číslo: '))
znamenko = input('Operace: ')


def funkce (a, b, operace):
    if operace == '+':
        return a + b
    elif operace == '-':
        return a - b
    elif operace == '*':
        return a*b
    elif operace == '/':
        return a/b
    else:
        print('Nerozumim zadani')


print(x, znamenko, y, '=', funkce(x,y,znamenko))

