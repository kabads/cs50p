import pytest
from jar import Jar

def test_create_jar():
    jar = Jar()
    assert jar.capacity == 12