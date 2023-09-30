import random


def main():
    level = get_level()

    #number of questions
    x = 10
    correct = 0

    #loop for 10 questions
    while x != 0:
        a, b = generate_integer(level)
        i = 0

        #loop to allow for 3 tries
        while True:
            answer = int(input(f'{a} + {b} = ' ))

            #if correct break out
            if answer == int(a) + int(b):
                x -= 1
                correct += 1
                break
            #if not remove 1 try
            else:
                i += 1
                #after 3 tries, show answer and break
                if i == 3:
                    print(f'{a} + {b} = {int(a) + int(b)}')
                    x -= 1
                    break
                else:
                    print('EEE')
    #after x questions show score
    else:
        print(f'Score: {correct}')


def get_level():
    while True:
        try:
            x = int(input('Level: '))
            if x in [1,2,3]:
                return x
            else:
                raise ValueError
        except:
            continue


def generate_integer(level):
    if level == 1:
        a = random.randint(0,9)
        b = random.randint(0,9)
        return a , b
    elif level == 2:
        a = random.randint(10,99)
        b = random.randint(10,99)
        return a , b
    elif level == 3:
        a = random.randint(100,999)
        b = random.randint(100,999)
        return a , b
    else:
        raise ValueError

if __name__ == "__main__":
    main()