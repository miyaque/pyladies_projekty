n = int(input('Zadejte cislo: '))


def faktorial(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result


def je_prvocislo(x):
    if x < 2:
        return '{} neni prvocislo'.format(x)
    elif x == 2:
        return '{} je prvocislo'.format(x)
    elif x % 2 == 0 and x > 2:
        return '{} neni prvocislo'.format(x)
    for i in range(3, x):
        if x % i == 0:
            return '{} neni prvocislo'.format(x)
    return '{} je prvocislo'.format(x)


def fibonacciho_posloupnost(n):
    x1 = 1
    x2 = 1
    print(x1)
    print(x2)
    for i in range(1, n + 1):
        soucet = x2 + x1
        print(soucet)
        x2, x1 = soucet, x2
