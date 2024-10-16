def main():
    fraction = input("Fraction: ")
    try:
        percentage = convert(fraction)
        print(gauge(percentage))
    except (ValueError, ZeroDivisionError):
        print("Invalid input")


def convert(fraction):
    try:
        X, Y = fraction.split("/")
        X, Y = int(X), int(Y)
        if X > Y:
            raise ValueError
        return round((X / Y) * 100)
    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
