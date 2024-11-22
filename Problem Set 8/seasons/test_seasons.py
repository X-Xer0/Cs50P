import pytest
from seasons import validate_date, get_minutes, minutes_to_words
from datetime import date, timedelta

def test_validate_date():

    assert validate_date("2022-01-01") == date(2022, 1, 1)

    with pytest.raises(ValueError):
        validate_date("2022/01/01")
    with pytest.raises(ValueError):
        validate_date("invalid")
    with pytest.raises(ValueError):
        validate_date("2022-13-01")

def test_minutes_to_words():
    assert minutes_to_words(1) == "One"
    assert minutes_to_words(1440) == "One thousand, four hundred forty"
    assert minutes_to_words(525600) == "Five hundred twenty-five thousand, six hundred"

def test_get_minutes():
    today = date.today()
    yesterday = today - timedelta(days=1)
    assert get_minutes(yesterday) == 1440

    one_year_ago = today.replace(year=today.year - 1)
    minutes = get_minutes(one_year_ago)
    assert 525600 <= minutes <= 527040
