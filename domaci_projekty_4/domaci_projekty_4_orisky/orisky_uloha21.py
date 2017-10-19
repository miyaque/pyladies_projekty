for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('bum-bac')
    elif i % 3 == 0:
        print('bum')
    elif i % 5 == 0:
        print('bac')
    else:
        print(i)
