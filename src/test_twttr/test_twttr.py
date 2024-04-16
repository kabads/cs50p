from twttr import shorten


def test_shorten():
    assert shorten("hello") == "hll"
    assert shorten("HELLO") == "HLL"
    # assert shorten("hello123") == "hll"
    # assert shorten("HELLO456") == "HLL"

def test_number():
    assert shorten("0") == "0"

def test_punctuation():
    assert shorten(".") == "."