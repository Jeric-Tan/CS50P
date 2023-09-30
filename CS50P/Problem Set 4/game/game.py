import random
import sys

while True:
    try:
        level = int(input('Level: '))
        number = random.randint(1 , level)
        while True:
            try:
                guess = int(input('Guess: '))
                if guess > 0:
                    if int(guess) == int(number):
                        print('Just right!')
                        sys.exit()
                    elif int(guess) < int(number):
                        print('Too small!')
                    elif int(guess) > int(number):
                        print('Too large!')

            except ValueError:
                continue
    except ValueError:
        continue

