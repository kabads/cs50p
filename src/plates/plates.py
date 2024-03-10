import re

def check_plate_length(plate):
    if len(plate) < 2 or len(plate) >6:
        # print(f"len plate: {len(plate)}")
        return False
    else:
        # print(f"len plate: {len(plate)}")
        return True


def has_alphabetic_after_digits(text):
    pattern = r'\[a-zA-Z]+d+'
    # print(f"has alphabetic after digits {bool(re.search(pattern, text))}")
    return bool(re.search(pattern, text))


def first_digit_check(text):
    pattern = r'0\d'
    # print(f"first digit check {bool(re.match(pattern, text))}")
    return bool(re.search(pattern, text))


def check_digit_char_digit(text):
    pattern = r'\d[a-zA-Z]\d'
    # print(f"check_digit_char_digit {not bool(re.match(pattern, text))}")
    return not bool(re.search(pattern, text))


def check_digits(plate):
    return not has_alphabetic_after_digits(plate) \
        and not first_digit_check(plate) \
            and check_digit_char_digit(plate)


def punctuation(text):
    pattern = r'\W'
    # print(f"punctuation {not bool(re.search(pattern, text))}")
    return not bool(re.search(pattern, text))


def start_two_letters(plate):
    return plate[0:2].isalpha()


def is_valid(plate):
    is_valid = True
    if not start_two_letters(plate):
        is_valid = False
        # print("Failed start two letters")
        return is_valid
    if not check_plate_length(plate):
        is_valid = False
        # print("Failed check_plate_lenght")
        return is_valid
    if not check_digits(plate) :
        is_valid = False
        # print("Failed check digits")
        return is_valid
    if not punctuation(plate):
        is_valid = False
        # print("Failed punctuation")
        return is_valid
    return is_valid


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

if __name__ == '__main__':
    main()

