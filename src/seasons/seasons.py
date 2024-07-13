from datetime import date
import inflect
import sys

p = inflect.engine()

def get_birthdate(dob):
    try:
        return date.fromisoformat(dob)
    except ValueError:
        sys.exit("Invalid date")

def get_age_in_days(birthdate):
    today = date.today()
    return (today - birthdate).days


def convert_minutes_to_word_minutes(minutes):
    return p.number_to_words(minutes, andword="").capitalize()


def main():
    days = get_age_in_days(get_birthdate(input("Date of Birth: ")))
    minutes = days * 24 * 60
    print(convert_minutes_to_word_minutes(minutes) + " minutes")


if __name__ == "__main__":
    main()