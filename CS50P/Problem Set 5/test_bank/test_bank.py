from bank import value

def test_bank():
    assert value('Hello') == 0
    assert value('hEllo my name is') == 0
    assert value('how you doing') == 20

def test_number():
    assert value('123') == 100

def test_punctuation():
    assert value(':hello?') == 100