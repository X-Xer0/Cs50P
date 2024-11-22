from datetime import date
import sys
import inflect

p = inflect.engine()

def validate_date(birth_date):
    """
    Validate date string and convert to date object.
    Raises ValueError if date format is invalid.
    """
    try:
        year, month, day = map(int, birth_date.split('-'))
        return date(year, month, day)
    except (ValueError, TypeError):
        raise ValueError("Invalid date format")

def get_minutes(birth_date):
    """
    Calculate minutes between birth_date and today.
    Returns the number of minutes as an integer.
    """
    today = date.today()
    diff = today - birth_date
    return round(diff.days * 24 * 60)

def minutes_to_words(minutes):
    """
    Convert minutes to words without 'and'.
    """
    return p.number_to_words(minutes, andword="").capitalize()

def main():
    try:
        birth_date = input("Date of Birth: ")
        date_obj = validate_date(birth_date)
        minutes = get_minutes(date_obj)
        print(f"{minutes_to_words(minutes)} minutes")
    except ValueError:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()
