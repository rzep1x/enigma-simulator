from enigma import Enigma
from components import Rotor, Plugboard, Reflector
import pytest

ROTORS_DATA = {
    "I": {
        "wiring": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
        "notch": "Q"
    },
    "II": {
        "wiring": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
        "notch": "E"
    },
    "III": {
        "wiring": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
        "notch": "V"
    },
    "IV": {
        "wiring": "ESOVPZJAYQUIRHXLNFTGKDCMWB",
        "notch": "J"
    },
    "V": {
        "wiring": "VZBRGITYUPSDNHLXAWMJQOFECK",
        "notch": "Z"
    }
}
REFLECTORS_DATA = {
    "B": "YRUHQSLDPXNGOKMIEBFZCWVJAT",
    "C": "FVPJIAOYEDRZXWGCTKUQSBNMHL"
}

#CREATE
def test_enigma_create():
    rotor1 = Rotor(
        wiring=ROTORS_DATA["I"]['wiring'], notch_position=ROTORS_DATA["I"]['notch'],
        initial_position='a'
    )
    rotor2 = Rotor(
        wiring=ROTORS_DATA["II"]['wiring'], notch_position=ROTORS_DATA["II"]['notch'],
        initial_position='a'
    )
    rotor3 = Rotor(
        wiring=ROTORS_DATA["III"]['wiring'], notch_position=ROTORS_DATA["III"]['notch'],
        initial_position='a'
    )

    reflector = Reflector(
        REFLECTORS_DATA["B"]
    )

    plugborad = Plugboard()

    enigma = Enigma(rotor1, rotor2, rotor3, reflector, plugborad)

    assert enigma.rotor1 == rotor1
    assert enigma.rotor2 == rotor2
    assert enigma.rotor3 == rotor3
    assert enigma.reflector == reflector
    assert enigma.plugboard == plugborad


def test_enigma_create_missing_component():
    rotor1 = Rotor(
        wiring=ROTORS_DATA["I"]['wiring'], notch_position=ROTORS_DATA["I"]['notch'],
        initial_position='a'
    )
    rotor2 = Rotor(
        wiring=ROTORS_DATA["II"]['wiring'], notch_position=ROTORS_DATA["II"]['notch'],
        initial_position='a'
    )
    rotor3 = Rotor(
        wiring=ROTORS_DATA["III"]['wiring'], notch_position=ROTORS_DATA["III"]['notch'],
        initial_position='a'
    )

    reflector = Reflector(
        REFLECTORS_DATA["B"]
    )

    with pytest.raises(TypeError):
        Enigma(rotor1, rotor2, rotor3, reflector)


# SETTERS
def test_enigma_set_rotor():
    rotor1 = Rotor(
        wiring=ROTORS_DATA["I"]['wiring'], notch_position=ROTORS_DATA["I"]['notch'],
        initial_position='a'
    )
    rotor2 = Rotor(
        wiring=ROTORS_DATA["II"]['wiring'], notch_position=ROTORS_DATA["II"]['notch'],
        initial_position='a'
    )
    rotor3 = Rotor(
        wiring=ROTORS_DATA["III"]['wiring'], notch_position=ROTORS_DATA["III"]['notch'],
        initial_position='a'
    )

    rotor4 = Rotor(
        wiring=ROTORS_DATA["IV"]['wiring'], notch_position=ROTORS_DATA["IV"]['notch'],
        initial_position='a'
    )

    reflector = Reflector(
        REFLECTORS_DATA["B"]
    )

    plugborad = Plugboard()

    enigma = Enigma(rotor1, rotor2, rotor3, reflector, plugborad)

    assert enigma.rotor1 == rotor1
    assert enigma.rotor2 == rotor2
    assert enigma.rotor3 == rotor3
    assert enigma.reflector == reflector
    assert enigma.plugboard == plugborad

    enigma.set_rotor1(rotor4)
    enigma.set_rotor2(rotor1)
    assert enigma.rotor1 == rotor4
    assert enigma.rotor2 == rotor1
    assert enigma.rotor3 == rotor3
    assert enigma.reflector == reflector
    assert enigma.plugboard == plugborad
    assert enigma.rotor1 == rotor1
    assert enigma.rotor2 == rotor2
    assert enigma.rotor3 == rotor3
    assert enigma.reflector == reflector
    assert enigma.plugboard == plugborad


def test_enigma_reflector_setter():
    rotor1 = Rotor(
        wiring=ROTORS_DATA["I"]['wiring'], notch_position=ROTORS_DATA["I"]['notch'],
        initial_position='a'
    )
    rotor2 = Rotor(
        wiring=ROTORS_DATA["II"]['wiring'], notch_position=ROTORS_DATA["II"]['notch'],
        initial_position='a'
    )
    rotor3 = Rotor(
        wiring=ROTORS_DATA["III"]['wiring'], notch_position=ROTORS_DATA["III"]['notch'],
        initial_position='a'
    )

    reflector = Reflector(
        REFLECTORS_DATA["B"]
    )

    reflector2 = Reflector(REFLECTORS_DATA['C'])
    plugborad = Plugboard()
    enigma = Enigma(rotor1, rotor2, rotor3, reflector, plugborad)

    assert enigma.rotor1 == rotor1
    assert enigma.rotor2 == rotor2
    assert enigma.rotor3 == rotor3
    assert enigma.reflector == reflector
    assert enigma.plugboard == plugborad
    enigma.set_reflector(reflector2)
    assert enigma.reflector == reflector2


def test_enigma_step():
    rotor1 = Rotor(
        wiring=ROTORS_DATA["I"]['wiring'], notch_position=ROTORS_DATA["I"]['notch'],
        initial_position='P'
    )
    rotor2 = Rotor(
        wiring=ROTORS_DATA["II"]['wiring'], notch_position=ROTORS_DATA["II"]['notch'],
        initial_position='d'
    )
    rotor3 = Rotor(
        wiring=ROTORS_DATA["III"]['wiring'], notch_position=ROTORS_DATA["III"]['notch'],
        initial_position='a'
    )
    reflector = Reflector(
        REFLECTORS_DATA["B"]
    )
    plugborad = Plugboard()

    enigma = Enigma(rotor1, rotor2, rotor3, reflector, plugborad)
    assert enigma.rotor1.current_position == 15
    assert enigma.rotor2.current_position == 3
    assert enigma.rotor3.current_position == 0
    enigma.step()
    assert enigma.rotor1.current_position == 16
    assert enigma.rotor2.current_position == 3
    assert enigma.rotor3.current_position == 0
    enigma.step()
    assert enigma.rotor1.current_position == 17
    assert enigma.rotor2.current_position == 4
    assert enigma.rotor3.current_position == 0
    enigma.step()
    assert enigma.rotor1.current_position == 18
    assert enigma.rotor2.current_position == 5
    assert enigma.rotor3.current_position == 1
