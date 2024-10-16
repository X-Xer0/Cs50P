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

    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == '0' and (i == 2 or (i > 2 and not s[i-1].isdigit())):
                return False
            if not s[i:].isdigit():
                return False
            break

    if not s.isalnum():
        return False

    return True

if __name__ == "__main__":
    main()
