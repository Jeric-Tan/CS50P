x = input('Expression: ')
a , b , c = x.split(' ')
if b == '+':
    print(f'{float(a) + float(c):.1f}')
elif b == "-":
    print(f'{float(a) - float(c):.1f}')
elif b == "*":
    print(f'{float(a) * float(c):.1f}')
elif b == "/":
    print(f'{float(a) / float(c):.1f}')