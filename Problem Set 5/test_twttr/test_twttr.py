import twttr

def test_shorten():
    assert twttr.shorten("Twitter") == "Twttr"
    assert twttr.shorten("HELLO") == "HLL"
    assert twttr.shorten("apple") == "ppl"
    assert twttr.shorten("AEIOUaeiou") == ""
    assert twttr.shorten("12345") == "12345"
    assert twttr.shorten("!@#$%") == "!@#$%"
    assert twttr.shorten("PyThOn") == "PyThn"
