import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):

    pattern = r'(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)'
    match = re.match(pattern, s)

    if not match:
        raise ValueError("Invalid format")

    start_hour, start_minute, start_period, end_hour, end_minute, end_period = match.groups()

    start_minute = start_minute or "00"
    end_minute = end_minute or "00"

    start_time_24 = to_24_hour_format(int(start_hour), int(start_minute), start_period)
    end_time_24 = to_24_hour_format(int(end_hour), int(end_minute), end_period)

    return f"{start_time_24} to {end_time_24}"

def to_24_hour_format(hour, minute, period):

    if period == "AM":
        if hour == 12:
            hour = 0
    elif period == "PM":
        if hour != 12:
            hour += 12

    if not (0 <= hour < 24 and 0 <= minute < 60):
        raise ValueError("Invalid time")

    return f"{hour:02}:{minute:02}"

if __name__ == "__main__":
    main()
