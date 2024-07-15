import pytest
from jar import Jar

def test_create_jar():
    jar = Jar()
    assert jar.capacity == 12


def test_deposit_jar():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(3)
    assert jar.size == 8
    jar.deposit(4)
    assert jar.size == 12


def test_withdraw_jar():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(5)
    assert jar.size == 0
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2