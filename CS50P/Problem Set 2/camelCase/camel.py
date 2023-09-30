text = input('camelCase: ')

print ('snake_case: ' , end = '')
for letter in text:
    if letter.isupper():
        print('_' + letter.lower(), end='')
    else:
        print(letter.lower(), end='')

print('')

