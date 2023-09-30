import sys
#whitespace , comments, docstrings
def main():
    initial_check()
    list = open_file()
    i = 0
    for word in list:
        if count_line(word) == True:
            i += 1
    print(i)

def initial_check():
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')

    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments' )

    elif not sys.argv[1].endswith('.py'):
        sys.exit('Not a Python File')

def open_file():
    try:
        with open(sys.argv[1]) as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        sys.exit('File does not exist')


def count_line(word):
    if word.strip() and not word.lstrip().startswith('#'):
        return True
    else:
        return False



main()