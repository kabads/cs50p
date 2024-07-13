from datetime import date
import inflect

p = inflect.engine()

def get_birthdate(dob):
    try:
        return date.fromisoformat(dob)
    except ValueError:
        return "Invalid date"

def get_age_in_days(birthdate):
    today = date.today()
    return (today - birthdate).days


def convert_minutes_to_word_minutes(minutes):
    return p.number_to_words(minutes).capitalize()


def main():
    # TODO need to check for format YYYY-MM-DD - and sys.exit if not
    birthdate = get_birthdate(input("Date of Birth: "))
    days = get_age_in_days(birthdate)
    # print(f"Days: {days}")
    hours = days * 24
    # print(f"Hours: {hours}")
    minutes = hours * 60
    # print(f"Minutes: {minutes}")
    # words = p.number_to_words(minutes)
    words = convert_minutes_to_word_minutes(minutes)
    print(words.capitalize() + " minutes")


if __name__ == "__main__":
    main()