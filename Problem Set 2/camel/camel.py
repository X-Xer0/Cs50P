def main():
    camel_case = input("Enter camelCase variable: ")
    print(to_snake_case(camel_case))

def to_snake_case(name):
    snake_case = ""
    for char in name:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    return snake_case

if __name__ == "__main__":
    main()
