from components import (
    Rotor, Reflector, Plugboard,
    RotorConfigurationInitialPositionError,
    RotorConfigurationWiringError,
    RotorConfigurationNotchPositionError,
)
import pytest


# Tests for Rotor
# Test create
def test_rotor_create_():
    rotor = Rotor(notch_position='A', wiring='EKMFLGDQVZNTOWYHXUSPAIBRCJ', initial_position='B', ring_setting='B')
    assert rotor.notch_position == 0
    assert rotor.initial_position == 1
    assert rotor.wiring == (
        [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
    )
    assert rotor.ring_setting == 1
    assert rotor.current_position == 1


def test_rotor_create_lower_notch_postion():
    rotor = Rotor(notch_position='a', wiring='EKMFLGDQVZNTOWYHXUSPAIBRCJ', initial_position='B', ring_setting='c')
    assert rotor.notch_position == 0
    assert rotor.initial_position == 1
    assert rotor.wiring == (
        [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
    )
    assert rotor.ring_setting == 2


def test_rotor_create_ring_setting_default():
    rotor = Rotor(notch_position='a', wiring='EKMFLGDQVZNTOWYHXUSPAIBRCJ', initial_position='B')
    assert rotor.notch_position == 0
    assert rotor.initial_position == 1
    assert rotor.wiring == (
        [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
    )
    assert rotor.ring_setting == 0


def test_rotor_create_wiring_lower():
    rotor = Rotor(notch_position='a', wiring='ekmflgdqvzntowyhxuspaibrcj', initial_position='B')
    assert rotor.notch_position == 0
    assert rotor.initial_position == 1
    assert rotor.wiring == (
        [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
    )


def test_rotor_create_notch_position_int():
    with pytest.raises(RotorConfigurationNotchPositionError):
        Rotor(notch_position=1, initial_position='c', wiring="EKMFLGDQVZNTOWYHXUSPAIBRCJ")


def test_rotor_create_notch_position_more_than_1():
    with pytest.raises(RotorConfigurationNotchPositionError):
        Rotor(notch_position='ab', initial_position='c', wiring="EKMFLGDQVZNTOWYHXUSPAIBRCJ")


def test_rotor_create_notch_position_is_not_alpha():
    with pytest.raises(RotorConfigurationNotchPositionError):
        Rotor(notch_position='!', initial_position='c', wiring="EKMFLGDQVZNTOWYHXUSPAIBRCJ")


def test_rotor_create_wiring_long_len():
    with pytest.raises(RotorConfigurationWiringError):
        Rotor(notch_position='a', wiring="EKMFLWYHXUSPAIBRCJ", initial_position='c')


def test_rotor_create_wiring_not_alpha():
    with pytest.raises(RotorConfigurationWiringError):
        Rotor(notch_position='a', wiring="EKMFLGDQVZNTO2YHXUSPAIBRC!", initial_position='c')


def test_rotor_create_wiring_is_number():
    with pytest.raises(RotorConfigurationWiringError):
        Rotor(notch_position='a', wiring=84710293847561029384756102, initial_position='c')


def test_rotor_create_wiring_is_str_of_nums():
    with pytest.raises(RotorConfigurationWiringError):
        Rotor(notch_position='a', wiring="84710293847561029384756102", initial_position='c')


def test_rotor_create_initial_position_not_alpha():
    with pytest.raises(RotorConfigurationInitialPositionError):
        Rotor(notch_position='a', initial_position='!', wiring="EKMFLGDQVZNTOWYHXUSPAIBRCJ")


def test_rotor_create_initial_position_wrong_length():
    with pytest.raises(RotorConfigurationInitialPositionError):
        Rotor(notch_position='a', initial_position='bc', wiring="EKMFLGDQVZNTOWYHXUSPAIBRCJ")


def test_rotor_create_initial_position_not_str():
    with pytest.raises(RotorConfigurationInitialPositionError):
        Rotor(notch_position='a', initial_position=1, wiring="EKMFLGDQVZNTOWYHXUSPAIBRCJ")


def test_rotor_create_non_ascii_characters():
    with pytest.raises(RotorConfigurationWiringError):
        Rotor(notch_position='A', wiring='EKMFLGDQVZNTOWYHXUSPAIBRCŁ', initial_position='B', ring_setting='B')


# Tests setters
def test_ring_setting_setter():
    rotor = Rotor(notch_position='A', wiring='EKMFLGDQVZNTOWYHXUSPAIBRCJ', initial_position='B', ring_setting='B')
    assert rotor.notch_position == 0
    assert rotor.initial_position == 1
    assert rotor.wiring == (
        [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
    )
    assert rotor.ring_setting == 1
    assert rotor.current_position == 1
    rotor.set_ring_setting(rotor.ring_setting + 1)
    assert rotor.ring_setting == 2


def test_ring_setting_setter_more_than_26():
    rotor = Rotor(notch_position='A', wiring='EKMFLGDQVZNTOWYHXUSPAIBRCJ', initial_position='B', ring_setting='B')
    assert rotor.notch_position == 0
    assert rotor.initial_position == 1
    assert rotor.wiring == (
        [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
    )
    assert rotor.ring_setting == 1
    assert rotor.current_position == 1
    rotor.set_ring_setting(27)
    assert rotor.ring_setting == 1


def test_set_current_postion():
    rotor = Rotor(notch_position='A', wiring='EKMFLGDQVZNTOWYHXUSPAIBRCJ', initial_position='B', ring_setting='B')
    assert rotor.notch_position == 0
    assert rotor.initial_position == 1
    assert rotor.wiring == (
        [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
    )
    assert rotor.ring_setting == 1
    assert rotor.current_position == 1
    rotor.set_current_position(rotor.current_position + 1)
    assert rotor.current_position == 2
    assert rotor.initial_position == 1


def test_set_initial_position():
    rotor = Rotor(notch_position='A', wiring='EKMFLGDQVZNTOWYHXUSPAIBRCJ', initial_position='B', ring_setting='B')
    assert rotor.notch_position == 0
    assert rotor.initial_position == 1
    assert rotor.wiring == (
        [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
    )
    assert rotor.ring_setting == 1
    assert rotor.current_position == 1
    rotor.set_initial_position(4)
    assert rotor.initial_position == 4
    assert rotor.current_position == 4


# Tests for Reflector
def test_reflector_create():
    reflector = Reflector(wiring='EKMFLGDQVZNTOWYHXUSPAIBRCJ')
    assert reflector.wiring == (
        [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
    )


# Tests for Plugboard
def test_plugboard_create():
    plug = Plugboard("ab cd fg")
    assert plug.connections == (
        [1, 0, 3, 2, 4, 6, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    )


def test_empty_plugboard_create():
    plug = Plugboard()
    assert plug.connections == [num for num in range(26)]


def test_plugboard_create_three_letters():
    with pytest.raises(ValueError):
        Plugboard('abc sx kw')


def test_plugborad_create_nonascii_letter():
    with pytest.raises(ValueError):
        Plugboard('dł ab po')


def test_plugborad_create_special_char():
    with pytest.raises(ValueError):
        Plugboard('d. c! po   a')


def test_plugboard_create_same_letters_used_more_than_one_time():
    with pytest.raises(ValueError):
        Plugboard("ab ac bc")