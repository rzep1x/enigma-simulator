from components import Rotor, Reflector
import pytest


def test_rotor_create():
    rotor = Rotor(notch_position='a', wiring='EKMFLGDQVZNTOWYHXUSPAIBRCJ', initial_poition='B')
    assert rotor.notch_position == 0
    assert rotor.initial_position == 1
    assert rotor.wiring == (
        [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
    ) 


def test_rotor_create_wrong_notch_position():
    with pytest.raises(ValueError):
        Rotor(notch_position=1, initial_poition='c', wiring="EKMFLGDQVZNTOWYHXUSPAIBRCJ")