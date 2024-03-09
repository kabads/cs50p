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
    # print(f"has alphabetic {bool(re.search(pattern, text))}")
    return not bool(re.search(pattern, text))

def first_digit_check(text):
    pattern = r'^0\d*'
    # print(f"first digit check {bool(re.match(pattern, text))}")
    return bool(re.match(pattern, text))


def check_digits(plate):
    is_valid = False
    if has_alphabetic_after_digits(plate) and first_digit_check(plate):
        is_valid = True
    return is_valid

def punctuation(text):
    pattern = r'\W'
    # print(f"punctuation {not bool(re.search(pattern, text))}")
    return not bool(re.search(pattern, text))

def is_valid(plate):
    is_valid = True
    if not check_plate_length(plate):
        is_valid = False
    if not check_digits(plate) :
        is_valid = False
    if not punctuation(plate):
        is_valid = False
    return is_valid


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

if __name__ == '__main__':
    main()

