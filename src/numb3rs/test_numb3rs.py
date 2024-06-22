from numb3rs import validate

def test_valid_ipv4():
  assert validate("127.0.0.1") == True
  assert validate("275.3.6.28") == False
  assert validate("1.2.3.4") == True
  assert validate("0.0.0.0") == True
  assert validate("02.0.0.0") == True

def test_invalid_ipv4():
  assert validate("255.456.0.0") == False