def convert(input_str):
    return input_str.replace(':)', '🙂').replace(':(', '🙁')

def main():
    input_str = input()
    print(convert(input_str))

if __name__ == "__main__":
    main()
