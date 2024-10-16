from plates import is_valid

def test_valid():
    assert is_valid("CS50") == True
    assert is_valid("AB123") == True
    assert is_valid("XYZ999") == True

def test_invalid_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False

def test_invalid_start():
    assert is_valid("50CS") == False
    assert is_valid("123ABC") == False
    assert is_valid("9CS") == False
    assert is_valid("C1") == False

def test_invalid_characters():
    assert is_valid("CS!50") == False
    assert is_valid("CS 50") == False

def test_zero_in_middle():
    assert is_valid("CS05") == False
    assert is_valid("AB012") == False

def test_number_placement():
    assert is_valid("ABC12D") == False
    assert is_valid("CS50Z") == False
