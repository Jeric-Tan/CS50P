from seasons import  check


def test_check():
    assert check('2021-04-19') == ('2021', '04', '19')
    assert check('2022-04-19') == ('2022', '04', '19')

    assert check('04-19-2023') == None