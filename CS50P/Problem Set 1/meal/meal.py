def main():
    x = input('What time? ')
    time = convert(x)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(time):
    a , b = time.split(":")
    c = float(a) + (float(b)/60)
    return c

if __name__ == "__main__":
    main()