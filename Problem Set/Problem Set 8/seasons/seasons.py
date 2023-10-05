from datetime import date
import sys
import inflect
import re

p = inflect.engine()

def main():

    txt = input('Date of Birth: ')
    try:
        year, month, day = check(txt)
        birth = date(int(year), int(month), int(day))
    except:
        sys.exit('Invalid date')

    today = date.today()
    result = today - birth
    minutes = int(result.total_seconds() / 60)
    if minutes > 0:
        words = p.number_to_words(minutes, andword='')
        print(f'{words.capitalize()} minutes')
    else:
        sys.exit('Date is too far')

def check(txt):
    if re.search(r'^[0-9]{4}-[0-1][0-9]-[0-3][0-9]$' , txt):
        year, month, day = txt.split('-')
        return year, month , day









if __name__ == "__main__":
    main()