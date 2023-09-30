
while True:
    txt = input('Fraction: ')

    try:
        a , b = txt.split('/')
        percentage = (int(a) / int(b)) * 100
        if 99 <= percentage <= 100:
            print('F')
            break
        elif percentage <= 1:
            print('E')
            break
        elif int(a) > int(b):
            pass

        else:
            print(f'{round(percentage)}%')
            break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
