from components import (
    Rotor, Reflector, Plugboard,
    RotorConfigurationError,
    PlugboardConfigurationError,
    ReflectorConfigurationError
)
import pytest


# Tests for Rotor
# Test create
def test_rotor_create_():
    rotor = Rotor(name='I', initial_position=1, ring_setting=1)
    assert rotor.notch_positions == [16]
    assert rotor.initial_position == 1
    assert rotor.wiring == (
        [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
    )
    assert rotor.ring_setting == 1
    assert rotor.current_position == 1


def test_rotor_create_ring_setting_default():
    rotor = Rotor(name='I', initial_position=1)
    assert rotor.notch_positions == [16]
    assert rotor.initial_position == 1
    assert rotor.wiring == (
        [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
    )
    assert rotor.ring_setting == 0


def test_rotor_create_initial_position_not_int():
    with pytest.raises(RotorConfigurationError):
        Rotor(name='I', initial_position='!')


def test_rotor_create_rotor_not_in_rotors_data():
    with pytest.raises(RotorConfigurationError):
        Rotor(name='VIII', initial_position='!')


def test_rotor_create_initial_position_wrong_length():
    with pytest.raises(RotorConfigurationError):
        Rotor(name='I', initial_position='bc')


def test_rotor_create_initial_position_not_int2():
    with pytest.raises(RotorConfigurationError):
        Rotor(name='I', initial_position='q')


def test_rotor_create_double_notch_postion():
    rotor = Rotor(name='VIII', initial_position=1, ring_setting=1)
    assert rotor.notch_positions == [25, 12]
    assert rotor.initial_position == 1
    assert rotor.wiring == (
        [5, 10, 16, 7, 19, 11, 23, 14, 2, 1, 9, 18, 15, 3, 25, 17, 0, 12, 4, 22, 13, 8, 20, 24, 6, 21]
    )
    assert rotor.ring_setting == 1
    assert rotor.current_position == 1


# Tests setters
def test_ring_setting_setter():
    rotor = Rotor(name='I', initial_position=1, ring_setting=1)
    assert rotor.notch_positions == [16]
    assert rotor.initial_position == 1
    assert rotor.wiring == (
        [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
    )
    assert rotor.ring_setting == 1
    assert rotor.current_position == 1
    rotor.set_ring_setting(rotor.ring_setting + 1)
    assert rotor.ring_setting == 2


def test_ring_setting_setter_more_than_26():
    rotor = Rotor(name='I', initial_position=1, ring_setting=1)
    assert rotor.notch_positions == [16]
    assert rotor.initial_position == 1
    assert rotor.wiring == (
        [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
    )
    assert rotor.ring_setting == 1
    assert rotor.current_position == 1
    rotor.set_ring_setting(27)
    assert rotor.ring_setting == 1


def test_set_current_postion():
    rotor = Rotor(name='I', initial_position=1, ring_setting=1)
    assert rotor.notch_positions == [16]
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
    rotor = Rotor(name='I', initial_position=1, ring_setting=1)
    assert rotor.notch_positions == [16]
    assert rotor.initial_position == 1
    assert rotor.wiring == (
        [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
    )
    assert rotor.ring_setting == 1
    assert rotor.current_position == 1
    rotor.set_initial_position(4)
    assert rotor.initial_position == 4
    assert rotor.current_position == 4


def test_rotor_step():
    rotor = Rotor(name='I', initial_position=0)
    assert rotor.notch_positions == [16]
    assert rotor.initial_position == 0
    assert rotor.wiring == (
        [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
    )
    assert rotor.ring_setting == 0
    assert rotor.current_position == 0
    rotor.step()
    assert rotor.current_position == 1
    rotor.step()
    assert rotor.current_position == 2


def test_rotor_step_current_position_26():
    rotor = Rotor(name='I', initial_position=25)
    assert rotor.notch_positions == [16]
    assert rotor.initial_position == 25
    assert rotor.wiring == (
        [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
    )
    assert rotor.ring_setting == 0
    assert rotor.current_position == 25
    rotor.step()
    assert rotor.current_position == 0


def test_rotor_is_at_notch():
    rotor = Rotor(name='I', initial_position=14)
    assert rotor.notch_positions == [16]
    assert rotor.initial_position == 14
    assert rotor.wiring == (
        [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
    )
    assert rotor.ring_setting == 0
    assert rotor.current_position == 14
    rotor.step()
    assert rotor.current_position == 15
    assert not rotor.is_at_notch()
    rotor.step()
    assert rotor.is_at_notch()


# Tests for Reflector
def test_reflector_create():
    reflector = Reflector(name='B')
    assert reflector.wiring == (
        [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]
    )


def test_reflector_create_not_in_reflectors_data():
    with pytest.raises(ReflectorConfigurationError):
        Reflector('a')


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
    with pytest.raises(PlugboardConfigurationError):
        Plugboard('abc sx kw')


def test_Plugboard_create_nonascii_letter():
    with pytest.raises(PlugboardConfigurationError):
        Plugboard('dł ab po')


def test_Plugboard_create_special_char():
    with pytest.raises(PlugboardConfigurationError):
        Plugboard('d. c! po   a')


def test_plugboard_create_same_letters_used_more_than_one_time():
    with pytest.raises(PlugboardConfigurationError):
        Plugboard("ab ac bc")
