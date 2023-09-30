from plates import is_valid

def test_length():
    assert is_valid('HELLOOO') == False
    assert is_valid('H') == False

def test_start():
    assert is_valid('44HEEE') == False
    assert is_valid('H3') == False

def test_middle():
    assert is_valid('CS50P') == False

def test_number():
    assert is_valid('CS50') == True
    assert is_valid('CS05') == False

def test_punctuation():
    assert is_valid('PI3.14') == False

