from twttr import shorten

def test_shorten():
    assert shorten("hELlo") == 'hLl'

def test_numbers():
    assert shorten("123456") == '123456'

def test_punctuation():
    assert shorten(': , ;.') == ': , ;.'
