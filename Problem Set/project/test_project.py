from project import discard, check, sort

def test_sort():
    hand = ['5🎋','3🎱','8🎋','5🀄','6🎋','3🎱','1🎱','7🎋','5🀄','3🎱','2🎱','5🀄','3🎱','8🎋']
    assert sort(hand) == ['5🎋','6🎋','7🎋','8🎋','8🎋','1🎱','2🎱','3🎱','3🎱','3🎱','3🎱','5🀄','5🀄','5🀄']

def test_check():
    hand = ['5🎋','3🎱','8🎋','5🀄','6🎋','3🎱','1🎱','7🎋','5🀄','3🎱','2🎱','5🀄','3🎱','8🎋']
    assert check(sort(hand)) == True

def test_discard():
    hand = ['5🎋','3🎱','8🎋','5🀄','6🎋','3🎱','1🎱','7🎋','5🀄','3🎱','2🎱','5🀄','3🎱','8🎋']
    assert discard(hand , 5) == ['5🎋','3🎱','8🎋','5🀄','3🎱','1🎱','7🎋','5🀄','3🎱','2🎱','5🀄','3🎱','8🎋']



