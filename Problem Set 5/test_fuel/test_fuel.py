import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    with pytest.raises(ValueError):
        convert("5/4")
    with pytest.raises(ValueError):
        convert("not/a/number")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"
    assert gauge(25) == "25%"
