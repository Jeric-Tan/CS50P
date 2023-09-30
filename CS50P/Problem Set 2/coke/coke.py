#while loop needed
#print amount
z = 50
print(f'Amount Due: {z}')


#Calculation
while z != 0:
    x = input('Insert Coin: ')
    if x == '25':
        z = z - 25

    elif x == '10':
        z = z - 10

    elif x == '5':
        z = z - 5

    if z <= 0:
        print(f'Change Owed: {-z}')
        break

    print(f'Amount Due: {z}')


