def main():
    text = input("Input: ")
    print(f"Output: {remove_vowels(text)}")

def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return "".join([char for char in text if char not in vowels])

if __name__ == "__main__":
    main()
