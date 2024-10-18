import csv
import sys

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py input.csv output.csv")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file) as file:
            reader = csv.DictReader(file)
            students = []

            for row in reader:
                last, first = row['name'].split(', ')
                students.append({"first": first, "last": last, "house": row["house"]})

        with open(output_file, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            writer.writerows(students)

    except FileNotFoundError:
        sys.exit(f"File {input_file} not found")

if __name__ == "__main__":
    main()
