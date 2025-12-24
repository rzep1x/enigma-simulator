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
