import sys

from PIL import Image, ImageOps

def main():
    initial_check()
    shirt = Image.open('shirt.png')
    person = open_file()
    size = shirt.size

    output = ImageOps.fit(person, size)
    output.paste(shirt , shirt)
    output.save(sys.argv[2])


def initial_check():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')

    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments' )

    elif not sys.argv[1].endswith(('.png','.jpg','.jpeg')):
        sys.exit('Invalid input')

    _ , x1 = sys.argv[1].split('.')
    _ , x2 = sys.argv[2].split('.')
    if not x1 == x2:
        sys.exit('Input and output have different extensions')

def open_file():
    try:
        person = Image.open(sys.argv[1])
        return person
    except FileNotFoundError:
        sys.exit('File cannot be found')





if __name__ == '__main__':
    main()

