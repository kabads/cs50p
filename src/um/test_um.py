from um import count
import pytest


def test_um():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album") == 1
    assert count("Um, thanks, um...") == 2
    assert count("hello, um, world") == 1