import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"

    match = re.search(pattern, ip)

    if match:
        octets = match.groups()

        for octet in octets:
            if not 0 <= int(octet) <= 255:
                return False
        return True
    return False

if __name__ == "__main__":
    main()
