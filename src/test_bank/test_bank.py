from bank import value

def test_value():
    assert value("hello") == 0
    assert value("hello world") == 0
    assert value("eueoau") == 100
    assert value("oEueA") == 100
    assert value("h") == 20
    assert value("hHht") != 0
    assert value("Good morning") == 100
    assert value("Hello") == 0