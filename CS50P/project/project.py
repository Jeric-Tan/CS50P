from tabulate import tabulate
import random
import re
import sys
import csv

def main():

    #Menu
    menu = {'Welcome to Mahjong' : ['Play' , 'Leaderboard' , 'Exit']}
    #Start Menu
    while True:
        print(tabulate(menu, headers='keys' , tablefmt='heavy_outline'))
        response = input("Select: Play | Leaderboard | Exit \n: ").strip().lower()
        if response == "play":
            print('\nStarting Game.........\n')
        #Play Game
            hand = sort(generate(14))
            username, num_turns = turn(hand)
            with open('highscore.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow((username,num_turns))
            print(f'Thank you for playing {username}!')

        elif response == 'leaderboard':
            print(tabulate(get_highscore(), headers=['No.' , 'Username' , 'Turns'] , tablefmt='fancy_grid' ))
        elif response == 'exit':
            sys.exit('Beep...Boop...Game Exiting')



#What happens in a turn
def turn(hand):
    num_turns = 0

    while True:
        #Checks for win condition
        if not check(hand) == True:
            num_turns += 1
            print(f'---Turn {num_turns}---')
            display(hand)
            #draw tile and prompt action
            draw = generate(1)
            print(f'Drawing Tile --> [{draw[0]}]')
            hand = action(hand, draw)
            check(hand)

        #After win condition is met
        else:
            print(f'Congrats! You have won!\nWinning hand was:')
            print(tabulate([hand], tablefmt='fancy_grid'))
            print('')

            #Checks for valid username
            while True:
                username = input('To save your score please key in a username: ')
                if username:
                    return username, num_turns
                else:
                    print('Please key in a valid Username')
#Display
def display(list):
    print(f'Current Hand:')
    print(tabulate([list], tablefmt='fancy_grid'))
    print('')


#Sorts hand
def sort(hand):
    a = []
    b = []
    c = []
    for i in hand:
            if re.findall(r'🎋' , i):
                a.append(i)
            elif re.findall(r'🎱' , i):
                b.append(i)
            elif re.findall(r'🀄' , i):
                c.append(i)
            else:
                break

    hand = sorted(a) + sorted(b) + sorted(c)
    return hand

#action
def action(hand, tile):
    while True:
        prompt1 = input('Keep or Discard? ')
        if prompt1.lower().strip() == 'k' or prompt1.lower().strip() == 'keep':
            while True:
                try:
                    prompt2 = int(input('\nChoose a tile to discard: '))
                    if 1 <= prompt2 <= len(hand):

                        hand = discard(hand, prompt2)
                        hand.append(tile[0])

                        break
                    else:
                        raise ValueError
                except ValueError:
                    print('Invalid Tile Number')
            return sort(hand)

        elif prompt1.lower().strip() == 'd' or prompt1.lower().strip() == 'discard' :
            discard(tile)
            return hand

        else:
            print("Invalid, try again")

#Randomly generates tiles
def generate(n):
    suit = ['🎱' , '🎋' , '🀄']
    list = []
    for _ in range(n):
        tile =  str(random.randint(1,9)) + random.choice(suit)
        list.append(tile)

    return list

#Discard tiles
def discard(list , n=0):

    discarded_card = list.pop(int(n)-1)
    print(f'You threw out [{discarded_card}]')
    print('\n---Ending Turn---\n')
    return list


#Win condition
def check(hand):
    no_sets = 0
    no_pairs = 0

    set = {}
    for tile in hand:
        if tile not in set:
            set[tile] = 1
        else:
            set[tile] += 1

    #consecutives
    for i in range(len(list(set))-2):
        if int(list(set)[i][0]) == int(list(set)[i+1][0]) -1 == int(list(set)[i+2][0]) -2:
            if set[list(set)[i]] > 0 and set[list(set)[i+1]] > 0 and set[list(set)[i+2]] > 0:
                no_sets += 1
                set[list(set)[i]] -= 1
                set[list(set)[i+1]] -= 1
                set[list(set)[i+2]] -= 1

    #triplets
    for tile in list(set):
        if set[tile] >= 3:
            set[tile] -= 3
            no_sets += 1

    #pairs
    for tile in list(set):
        if no_sets == 4 and set[tile] == 2:
            no_pairs += 1

    #win condition 4 sets 1 pair
    if no_sets == 4 and no_pairs == 1:
        return True

#Highscore
def get_highscore():
    list = []
    with open('highscore.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            list.append(row)

    list.sort(key=lambda x:int(x[1]))
    final_list =[]
    for i, highscore in enumerate(list,1):
        list = [i, highscore[0], int(highscore[1])]
        final_list.append(list)

    return final_list

if __name__ == '__main__':
    main()