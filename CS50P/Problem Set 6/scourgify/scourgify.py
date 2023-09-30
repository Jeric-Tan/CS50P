import sys
import csv

def main():
    initial_check()
    lines = open_file()
    final = (format(lines))
    output(final)

def initial_check():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')

    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments' )

    elif not sys.argv[1].endswith('.csv'):
        sys.exit(f'Could not be read {sys.argv[1]}')

def open_file():
    try:
        lines = []
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                lines.append({'name' : row['name'] , 'house' : row['house']})
            return lines
    except FileNotFoundError:
        sys.exit('File does not exist')

def format(lines):
    output_list = []
    for item in lines:
        last , first = item['name'].split(',')
        output_list.append({'first' : first.strip() , 'last' : last.strip() , 'house' : item['house']})
    return output_list

def output(final):
    try:
        with open(sys.argv[2], 'w') as file:
            writer = csv.DictWriter(file, fieldnames=['first','last','house'])
            writer.writeheader()

            for item in final:
                writer.writerow(item)

    except FileNotFoundError:
        sys.exit('File does not exist')

if __name__ == '__main__':
    main()