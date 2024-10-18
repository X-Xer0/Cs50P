import csv
import sys
from tabulate import tabulate

def main():
    if len(sys.argv) != 2 or not sys.argv[1].endswith('.csv'):
        sys.exit("Usage: python pizza.py <file.csv>")

    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            table = [row for row in reader]
    except FileNotFoundError:
        sys.exit(f"File {sys.argv[1]} not found")

    print(tabulate(table[1:], headers=table[0], tablefmt="grid"))

if __name__ == "__main__":
    main()
