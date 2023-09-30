import sys
from validator_collection import checkers

email = input("What's your email address? " )
try:
    is_valid = checkers.is_email(email)


    if is_valid == True:
        print('Valid')

    else:
        print('Invalid')

except ValueError:
    sys.exit('Invalid')