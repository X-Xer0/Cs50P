def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        date_input = input("Date: ").strip()

        if '/' in date_input:
            try:
                month, day, year = map(int, date_input.split('/'))
                if 1 <= month <= 12 and 1 <= day <= 31 and year >= 0:
                    print(f"{year:04}-{month:02}-{day:02}")
                    break
            except ValueError:
                pass

        else:
            try:
                month_day, year = date_input.rsplit(' ', 1)
                month_name, day = month_day.split(' ', 1)

                if not day.endswith(','):
                    continue

                day = day.rstrip(',')
                month = months.index(month_name) + 1
                day = int(day)

                if 1 <= month <= 12 and 1 <= day <= 31 and year.isdigit() and int(year) >= 0:
                    print(f"{year:04}-{month:02}-{day:02}")
                    break
            except (ValueError, IndexError):
                pass

        print("Invalid date. Please try again.")

main()
