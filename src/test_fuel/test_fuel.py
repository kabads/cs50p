from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/2") == 50
    with pytest.raises(ValueError):
        convert("a/b")
    with pytest.raises(ValueError):
        convert("10/5")
    with pytest.raises(ZeroDivisionError):
        convert("5/0")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(75) == "75%"