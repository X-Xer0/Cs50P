import sys
import os

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python lines.py <filename>")

    filename = sys.argv[1]

    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    if not os.path.isfile(filename):
        sys.exit("File does not exist")

    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            code_lines = count_code_lines(lines)
            print(code_lines)
    except FileNotFoundError:
        sys.exit("File not found")

def count_code_lines(lines):
    count = 0
    for line in lines:
        stripped_line = line.lstrip()
        if stripped_line and not stripped_line.startswith("#"):
            count += 1
    return count

if __name__ == "__main__":
    main()
