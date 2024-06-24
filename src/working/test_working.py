from working import convert
import pytest


def test_convert():
    assert convert("12 PM to 1 PM") == "12:00 to 13:00"
    assert convert("12 AM to 1 PM") == "00:00 to 13:00"
    assert convert("9AM to 5PM") == "09:00 to 17:00"


def test_value_error():
    with pytest.raises(ValueError):
        convert("12 pm to 1 pm")