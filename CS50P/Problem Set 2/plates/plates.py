def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
#vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    if len(s) < 2 or len(s) > 6 :
        return False

#All vanity plates must start with at least two letters.
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False


#Numbers cannot be used in the middle of a plate; they must come at the end.
    for i in range(len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False
#The first number used cannot be a ‘0’.”
    list = []
    for i in range(len(s)):
        if s[i].isdigit():
            list.append(s[i])
            if list[0] == '0':
                return False

#No periods, spaces, or punctuation marks are allowed
    if not s.isalnum():
        return False


    else:
        return True
main()