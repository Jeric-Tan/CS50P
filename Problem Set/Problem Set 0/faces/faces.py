def main():
    x = input()
    y = convert (x)
    print(y)

def convert(to):
    x = to.replace(':)','🙂')
    y = x.replace(':(','🙁')
    return y

main()