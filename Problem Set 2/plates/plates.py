def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False

    if not s[0:2].isalpha():
        return False

    number_started = False
    for i, char in enumerate(s):
        if char.isdigit():
            if not number_started:
                if char == '0':
                    return False
                number_started = True
        elif number_started:
            return False

    if not s.isalnum():
        return False

    return True


main()
