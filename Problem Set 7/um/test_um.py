from um import count

def test_single_um():
    assert count("um") == 1

def test_multiple_ums():
    assert count("um, um, um") == 3

def test_no_um():
    assert count("yummy") == 0

def test_mixed_case_um():
    assert count("Um, UM, um") == 3

def test_um_in_sentence():
    assert count("hello, um, how are you?") == 1

def test_um_as_substring():
    assert count("aluminum") == 0
