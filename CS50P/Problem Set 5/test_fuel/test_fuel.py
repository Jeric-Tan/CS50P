import pytest
from fuel import convert, gauge


def test_convert():
    assert convert('1/3') == 33

    with pytest.raises(ValueError):
        convert('cat/dog')
    with pytest.raises(ValueError):
        convert('4/3')
    with pytest.raises(ZeroDivisionError):
        convert('5/0')

def test_gauge():
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'
    assert gauge(20) == '20%'