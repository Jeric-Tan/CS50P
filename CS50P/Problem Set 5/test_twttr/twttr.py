def main():
    word = input('Input: ')
    print('Output: ' , end = '')
    print(shorten(word))


def shorten(word):
    x = ''
    for letter in word:
        if not letter.lower() in ['a' ,'e' , 'i' , 'o' , 'u']:
            x += letter
    return x



if __name__ == "__main__":
    main()
