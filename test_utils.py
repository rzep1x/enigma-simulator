from utils import char_to_int, int_to_char


def test_char_to_int():
    assert char_to_int('a') == 0
    assert char_to_int('A') == 0


def test_int_to_char():
    assert int_to_char(0) == 'A'
    assert int_to_char(2) == 'C'
