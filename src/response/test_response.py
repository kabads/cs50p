from response import validate

def test_validate():
    assert validate("adam@gmail.com") == True
