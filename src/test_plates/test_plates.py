from plates import is_valid

def main():
    test_is_valid_length()


# Plates may contain a maximum of 6 characters and a minimum of 2 characters.
def test_is_valid_length():
    assert is_valid("AB123C") == True
    assert is_valid("A") == False

# Plates must start with two letters.
def test_is_valid_start_two_letters():
    assert is_valid("AB123C") == True
    assert is_valid("1AB123C") == False

# Numbers cannot be used in the middle of a plate; they must come at the end
def test_is_valid_numbers_at_end():
    assert is_valid("AB123C") == True
    assert is_valid("AB1C23") == False

# The first number used cannot be a '0'

def test_is_valid_first_number_not_zero():
    assert is_valid("AB123C") == True
    assert is_valid("0B0123C") == False

# No periods, spaces, or punctuation marks are allowed in the plate.
def test_is_valid_no_punctuation():
    assert is_valid("AB123C") == True
    assert is_valid("AB123.C") == False

if __name__ == '__main__':
    main()
    print('All tests passed!')