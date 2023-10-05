def main():
    while True:
        try:
            text = input('Fraction: ')
            percentage = convert(text)
            print(gauge(percentage))
            break
        except (ValueError , ZeroDivisionError):
            pass


def convert(fraction):
    x , y = fraction.split('/')
    percentage = round((int(x) / int(y)) * 100)
    if int(y) == 0:
        raise ZeroDivisionError
    if int(x) > int(y):
        raise ValueError
    elif x.isdigit() == False or y.isdigit() == False:
        raise ValueError

    else:

        return percentage

def gauge(percentage):
    if int(percentage) <= 1:
        return f'E'
    elif int(percentage) >= 99:
        return f'F'
    else:
        return f'{percentage}%'

if __name__ == "__main__":
    main()

