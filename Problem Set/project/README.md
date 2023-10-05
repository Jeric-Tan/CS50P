# **Mahjong Minigame**

### This is my [CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python/2022/) final project submission. This is also my first ever project I have coded! Was inspired by the original game (which is WAYY more complicated) which my friends and I would play over the Lunar New Year.

#
### A simplified game of mahjong using Python.
### [Video Demo](https://youtu.be/zdoYFt3JnUI)

&nbsp;

# Installation
### Use [pip](https://pip.pypa.io/en/stable/) to install the packadge `tabulate` and `wcwidth`

&nbsp;

# Usage
### Use [python](https://www.python.org) to run the application
```
python project.py
```
### After which the start menu will show up and prompt the user for an *action*.
```
| Welcome to MajongSimulator |
|----------------------------|
| Play                       |
| Highscore                  |
| Exit                       |
Select: Play | Highscore | Exit
:
```
 ## Play
### A set of random **14 Tiles** are generated. This is your starting hand.
### Tiles contain both a **number** - from 1 to 9, and a **suit** - 🎱🎋🀄
```
---Turn 1---
Current Hand:
|1🎋|8🎋|3🎱|5🎱|5🎱|1🀄|2🀄|3🀄|5🀄|5🀄|6🀄|7🀄|8🀄|9🀄|
```
### After wards Tiles will be generated at random and user will be prompt on whether to keep or discard the tile.
```
Drawing Tile --> [1🎋]
Keep or Discard?
```
### Keep: Replaces a Tile in the user's hand with the randomly drawn Tile. Hand changes by 1 tile
### Discard: Discards the randomly drawn Tile. Hand does not change


&nbsp;
### **Win condition**: Gather **4** Sets of Triplets **and/or** Consecutives along with **1** ending Pair
#### Example:
```
|5🎋|6🎋|7🎋|8🎋|8🎋||1🎱|2🎱|3🎱|3🎱|3🎱|3🎱|5🀄|5🀄|5🀄|
```
### After winning, users will be prompt to give a **Username** which, together with the number of **Turns** it took them to win, will then be saved to a highscore [CSV File](https://docs.python.org/3/library/csv.html).
```
Congrats! You have won!
Winning hand was:
|5🎋|6🎋|7🎋|8🎋|8🎋|1🎱|2🎱|3🎱|3🎱|3🎱|3🎱|5🀄|5🀄|5🀄|

To save your score please key in a Username:
```
&nbsp;
## Leaderboard
### Shows the current highscores on the game
```
| No. | Username | Turns |
|-----|----------|-------|
|   1 | john     |     3 |
|   2 | peter    |    14 |
|   3 | jane     |    34 |
```
 ## Exit
 ### [sys.exit](https://docs.python.org/3/library/sys.html#sys.exit) will be called
```
Beep...Boop...Game Exiting
```

