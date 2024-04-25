from calculator import square
import pytest

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_zero():
    assert square(0) == 0

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_type_error():
    with pytest.raises(TypeError):
         square("cat") 

# Too long version:
""" def main():
    test_square()


def test_square():
    # if square(2) != 4:
    #     print("2 squared was not 4")
    # if square(3) != 9:
    #     print("3 squared was not 9")
    try:
        assert(square(2) == 4)
        assert(square(3) == 9)
    except AssertionError:
        print("Test failed")
        return
 """
