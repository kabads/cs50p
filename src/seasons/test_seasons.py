from unittest.mock import patch
from seasons import get_birthdate, get_age_in_days, convert_minutes_to_word_minutes
from datetime import date


def test_get_birthdate():
    assert get_birthdate("2020-01-01") == date(2020, 1, 1)
    assert get_birthdate("1995-12-31") == date(1995, 12, 31)
    assert get_birthdate("2005-06-15") == date(2005, 6, 15)
    assert get_birthdate("1980-11-25") == date(1980, 11, 25)
    assert get_birthdate("1975-02-28") == date(1975, 2, 28)


def test_get_age_in_days():
    with patch('seasons.date') as mock_date:
        mock_date.today.return_value = date(2023, 4, 1)
        birthdate = date(2000, 4, 1)
        expected_days = 23 * 365 + 5
        assert get_age_in_days(birthdate) == expected_days

        mock_date.today.return_value = date(2000, 1, 1)
        birthdate = date(1999, 1, 1)
        expected_days = 365
        assert get_age_in_days(birthdate) == expected_days


def test_convert_minutes_to_word_minutes():
    assert convert_minutes_to_word_minutes(1) == "One"
    assert convert_minutes_to_word_minutes(10) == "Ten"
    assert convert_minutes_to_word_minutes(525600) == "Five hundred twenty-five thousand, six hundred"