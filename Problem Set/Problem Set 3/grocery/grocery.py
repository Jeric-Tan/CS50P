dict = {}

while True:
    try:
        txt = input().strip().lower()

        if txt in dict:
            dict[txt] += 1
        else:
            dict[txt] = 1

    except EOFError:
        print()
        for key in sorted(dict.keys()):
            print(dict[key] , (key.upper()))
        break