from response import validate
import unittest

def test_validate():
    assert validate("adam@gmail.com") == True
    assert validate("adam@monkeez.org") == True
