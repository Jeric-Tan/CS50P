import re
import sys


def main():
    s = input('Text: ').strip()
    print(count(s))


def count(s):
    if matches := re.findall(r'\bum\b' , s , re.IGNORECASE):
        return len(matches)
    else:
        return 0




if __name__ == "__main__":
    main()