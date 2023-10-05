import re

def main():
    s = input('HTML: ').strip()
    print(parse(s))


def parse(s):
    if matches := re.search(r'<iframe (.*)src="https?://(www\.)?[A-Za-z]+\.[A-Za-z]+/[A-Za-z]+/([A-Za-z0-9]+)".*></iframe>' , s ):
        return f'https://youtu.be/{matches.group(3)}'



...


if __name__ == "__main__":
    main()