from numb3rs import validate

def test_valid_addresses():
    assert validate("192.168.1.1") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True

def test_invalid_addresses():
    assert validate("275.3.6.28") == False
    assert validate("192.168.1") == False
    assert validate("192.168.1.256") == False
    assert validate("192.168.1.-1") == False
    assert validate("192.168.1.abc") == False
    assert validate("300.300.300.300") == False
    assert validate("192.168.1.1.1") == False
