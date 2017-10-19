n = int(input('Zadejte cislo: '))


def sudost(x):
    if x % 2 == 0:
        return 'Cislo {} je sude.'.format(x)
    else:
        return 'Cislo {} je liche.'.format(x)


print(sudost(n))
