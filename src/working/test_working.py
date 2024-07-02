from working import convert
import pytest


def test_convert():
    assert convert("12 PM to 1 PM") == "12:00 to 13:00"
    assert convert("12 AM to 1 PM") == "00:00 to 13:00"
    assert convert("12:00 AM to 05:00 PM") == "00:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 PM to 5 PM") == "21:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("8 PM to 8 AM") == "20:00 to 08:00"
    assert convert("8:00 PM to 8:00 AM") == "20:00 to 08:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"


def test_value_error():
    with pytest.raises(ValueError):
        convert("12 pm to 1 pm")
    with pytest.raises(ValueError):
        convert("9AM to 5PM")