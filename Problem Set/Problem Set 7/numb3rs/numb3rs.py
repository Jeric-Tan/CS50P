import re


def main():
    ip = input("IPv4 Address: ").strip()
    print(validate(ip))


def validate(ip):
    if matches := re.search(r'^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$' , ip):

        if 0 <= int(matches.group(1)) | int(matches.group(2)) | int(matches.group(3)) | int(matches.group(4)) <= 255:
            return True
        else:
            return False

    else:
        return False


...


if __name__ == "__main__":
    main()