import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()


#Expects zero or two command-line arguments
if len(sys.argv) == 1:
    x = input('Input: ')
    f = Figlet(font = random.choice(fonts))
    print (print(f.renderText(x)))

elif len(sys.argv) == 3:
    if sys.argv[2] in fonts and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
        x = input('Input: ')
        f = Figlet(font = sys.argv[2])
        print(f.renderText(x))
    else:
        sys.exit('Invalid usage')
else:
    sys.exit('Invalid usage')