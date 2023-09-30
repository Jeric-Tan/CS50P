#list
list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
#continuous loop
while True:
    txt = input('Date: ')
    try:
        #split via "/" MM DD YYYY
        if '/' in txt:
            a , b , c = txt.split('/')
            if int(a) > 12 or int(b) > 31:
                pass
            else:
                print(f'{int(c) :04}-{int(a) :02}-{int(b) :02}')
                break

        #split via " "
        elif ',' in txt:
            x , y , z = txt.split()
            y = y.replace(',' , '')
            if x in list:
                month = int(list.index(x) + 1)

                if int(month) > 12 or int(y) > 31:
                    pass
                else:
                    print (f'{z}-{month:02}-{int(y):02}')
                    break

    except ValueError:
        pass