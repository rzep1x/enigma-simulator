from components import (
    Rotor, Reflector,
    RotorConfigurationInitialPositionError,
    RotorConfigarationWiringError,
    RotorConfigurationNotchPositionError,
)
import pytest


# Tests for Rotor
def test_rotor_create_():
    rotor = Rotor(notch_position='A', wiring='EKMFLGDQVZNTOWYHXUSPAIBRCJ', initial_poition='B', ring_setting='B')
    assert rotor.notch_position == 0
    assert rotor.initial_position == 1
    assert rotor.wiring == (
        [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
    )
    assert rotor.ring_setting == 1


def test_rotor_create_lower_notch_postion():
    rotor = Rotor(notch_position='a', wiring='EKMFLGDQVZNTOWYHXUSPAIBRCJ', initial_poition='B', ring_setting='c')
    assert rotor.notch_position == 0
    assert rotor.initial_position == 1
    assert rotor.wiring == (
        [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
    )
    assert rotor.ring_setting == 2


def test_rotor_create_ring_setting_default():
    rotor = Rotor(notch_position='a', wiring='EKMFLGDQVZNTOWYHXUSPAIBRCJ', initial_poition='B')
    assert rotor.notch_position == 0
    assert rotor.initial_position == 1
    assert rotor.wiring == (
        [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
    )
    assert rotor.ring_setting == 0


def test_rotor_create_wiring_lower():
    rotor = Rotor(notch_position='a', wiring='ekmflgdqvzntowyhxuspaibrcj', initial_poition='B')
    assert rotor.notch_position == 0
    assert rotor.initial_position == 1
    assert rotor.wiring == (
        [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
    )


def test_rotor_create_notch_position_int():
    with pytest.raises(RotorConfigurationNotchPositionError):
        Rotor(notch_position=1, initial_poition='c', wiring="EKMFLGDQVZNTOWYHXUSPAIBRCJ")


def test_rotor_create_notch_position_more_than_1():
    with pytest.raises(RotorConfigurationNotchPositionError):
        Rotor(notch_position='ab', initial_poition='c', wiring="EKMFLGDQVZNTOWYHXUSPAIBRCJ")


def test_rotor_create_notch_position_is_not_alpha():
    with pytest.raises(RotorConfigurationNotchPositionError):
        Rotor(notch_position='!', initial_poition='c', wiring="EKMFLGDQVZNTOWYHXUSPAIBRCJ")


def test_rotor_create_wiring_long_len():
    with pytest.raises(RotorConfigarationWiringError):
        Rotor(notch_position='a', wiring="EKMFLWYHXUSPAIBRCJ", initial_poition='c')


def test_rotor_create_wiring_not_alpha():
    with pytest.raises(RotorConfigarationWiringError):
        Rotor(notch_position='a', wiring="EKMFLGDQVZNTO2YHXUSPAIBRC!", initial_poition='c')


def test_rotor_create_wiring_is_number():
    with pytest.raises(RotorConfigarationWiringError):
        Rotor(notch_position='a', wiring=84710293847561029384756102, initial_poition='c')


def test_rotor_create_wiring_is_str_of_nums():
    with pytest.raises(RotorConfigarationWiringError):
        Rotor(notch_position='a', wiring="84710293847561029384756102", initial_poition='c')


def test_rotor_create_initial_position_not_alpha():
    with pytest.raises(RotorConfigurationInitialPositionError):
        Rotor(notch_position='a', initial_poition='!', wiring="EKMFLGDQVZNTOWYHXUSPAIBRCJ")


def test_rotor_create_initial_position_wrong_length():
    with pytest.raises(RotorConfigurationInitialPositionError):
        Rotor(notch_position='a', initial_poition='bc', wiring="EKMFLGDQVZNTOWYHXUSPAIBRCJ")


def test_rotor_create_initial_position_not_str():
    with pytest.raises(RotorConfigurationInitialPositionError):
        Rotor(notch_position='a', initial_poition=1, wiring="EKMFLGDQVZNTOWYHXUSPAIBRCJ")


# Tests for Reflector
def test_reflector_create():
    reflector = Reflector(wiring='EKMFLGDQVZNTOWYHXUSPAIBRCJ')
    assert reflector.wiring == (
        [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
    )
