import sys
from tabulate import tabulate

def main():
    initial_check()
    list = open_file(sys.argv[1])
    header = format(list)[0]

    print(tabulate((format(list[1:])),header, tablefmt='grid'))

def initial_check():
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')

    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments' )

    elif not sys.argv[1].endswith('.csv'):
        sys.exit('Not a CSV File')

def open_file(file):
    try:
        with open(file) as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        sys.exit('File does not exist')

def format(list):
    line = []
    for word in list:
        a , b , c = word.strip().split(',')
        line.append((a,b,c))

    return (line)



if __name__ == '__main__':
    main()