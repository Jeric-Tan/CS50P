x = input('Input: ')
print('Output: ' , end = '')
for letter in x:
    if letter.lower() in ['a' ,'e' , 'i' , 'o' , 'u']:
        x.replace(letter, '')
    else:
        print(letter , end ='')
print()