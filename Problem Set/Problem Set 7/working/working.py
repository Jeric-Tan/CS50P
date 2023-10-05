import re
import sys


def main():
    s = input('Hours: ').strip()
    print(convert(s))

def convert(s):
    if matches := re.search(r'([0-9]+):?([0-9]++)? (AM|PM) to ([0-9]+):?([0-9]++)? (AM|PM)' , s):

        f_hour = int(matches.group(1))
        s_hour = int(matches.group(4))
        # hours does not exceed 12hours
        if (f_hour or s_hour) > 12:
            raise ValueError
        if matches.group(3) == 'AM' and f_hour == 12:
            f_hour -= 12
        elif matches.group(3) == 'PM' and f_hour < 12:
            f_hour += 12


        if matches.group(6) == 'AM' and s_hour == 12:
            s_hour -= 12
        elif matches.group(6) == 'PM' and s_hour < 12:
            s_hour += 12



        if not (matches.group(2) or matches.group(5)) == None:
            f_minute , s_minute = int(matches.group(2)) , int(matches.group(5))
            # minutes does not exceed 60minutes
            if (f_minute or s_minute) >= 60:
                raise ValueError
            else:
                return f'{f_hour:02}:{f_minute:02} to {s_hour:02}:{s_minute:02}'

        else:
            return f'{f_hour:02}:00 to {s_hour:02}:00'
    else:
        raise ValueError


if __name__ == "__main__":
    main()