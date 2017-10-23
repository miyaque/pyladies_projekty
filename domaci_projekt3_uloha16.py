prvni_cislo = int(input('První číslo: '))
druhe_cislo = int(input('Druhé číslo: '))
znamenko = input('Operace: ')


def operace_nad_cisly(a, b, operace):
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


print(prvni_cislo, znamenko, druhe_cislo, '=', operace_nad_cisly(prvni_cislo, druhe_cislo, znamenko))
