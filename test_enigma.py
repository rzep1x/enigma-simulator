from enigma import Enigma
from components import Rotor, Plugboard, Reflector
import pytest
from utils import char_to_int

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


# CREATE
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
        initial_position='v'
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


def test_enigma_step_nothing_on_notch():
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
    assert enigma.rotor1.current_position == 0
    assert enigma.rotor2.current_position == 0
    assert enigma.rotor3.current_position == 0
    enigma.step()
    assert enigma.rotor1.current_position == 0
    assert enigma.rotor2.current_position == 0
    assert enigma.rotor3.current_position == 1


def test_enigma_step_first_rotor_on_notch():
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
        initial_position='v'
    )
    reflector = Reflector(
        REFLECTORS_DATA["B"]
    )
    plugborad = Plugboard()

    enigma = Enigma(rotor1, rotor2, rotor3, reflector, plugborad)
    assert enigma.rotor1.current_position == 0
    assert enigma.rotor2.current_position == 0
    assert enigma.rotor3.current_position == 21
    enigma.step()
    assert enigma.rotor1.current_position == 0
    assert enigma.rotor2.current_position == 1
    assert enigma.rotor3.current_position == 22


def test_enigma_step_second_rotor_on_notch():
    rotor1 = Rotor(
        wiring=ROTORS_DATA["I"]['wiring'], notch_position=ROTORS_DATA["I"]['notch'],
        initial_position='a'
    )
    rotor2 = Rotor(
        wiring=ROTORS_DATA["II"]['wiring'], notch_position=ROTORS_DATA["II"]['notch'],
        initial_position='e'
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
    assert enigma.rotor1.current_position == 0
    assert enigma.rotor2.current_position == 4
    assert enigma.rotor3.current_position == 0
    enigma.step()
    assert enigma.rotor1.current_position == 1
    assert enigma.rotor2.current_position == 5
    assert enigma.rotor3.current_position == 1


def test_enigma_step_third_rotor_on_notch():
    rotor1 = Rotor(
        wiring=ROTORS_DATA["I"]['wiring'], notch_position=ROTORS_DATA["I"]['notch'],
        initial_position='q'
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
    assert enigma.rotor1.current_position == 16
    assert enigma.rotor2.current_position == 0
    assert enigma.rotor3.current_position == 0
    enigma.step()
    assert enigma.rotor1.current_position == 16
    assert enigma.rotor2.current_position == 0
    assert enigma.rotor3.current_position == 1


def test_enigma_step_double_step():
    rotor1 = Rotor(
        wiring=ROTORS_DATA["I"]['wiring'], notch_position=ROTORS_DATA["I"]['notch'],
        initial_position='a'
    )
    rotor2 = Rotor(
        wiring=ROTORS_DATA["II"]['wiring'], notch_position=ROTORS_DATA["II"]['notch'],
        initial_position='d'
    )
    rotor3 = Rotor(
        wiring=ROTORS_DATA["III"]['wiring'], notch_position=ROTORS_DATA["III"]['notch'],
        initial_position='u'
    )
    reflector = Reflector(
        REFLECTORS_DATA["B"]
    )
    plugborad = Plugboard()

    enigma = Enigma(rotor1, rotor2, rotor3, reflector, plugborad)
    assert enigma.rotor1.current_position == 0
    assert enigma.rotor2.current_position == 3
    assert enigma.rotor3.current_position == 20
    enigma.step()
    assert enigma.rotor1.current_position == 0
    assert enigma.rotor2.current_position == 3
    assert enigma.rotor3.current_position == 21
    enigma.step()
    assert enigma.rotor1.current_position == 0
    assert enigma.rotor2.current_position == 4
    assert enigma.rotor3.current_position == 22
    enigma.step()
    assert enigma.rotor1.current_position == 1
    assert enigma.rotor2.current_position == 5
    assert enigma.rotor3.current_position == 23


def test_basic_encryption():
    r1 = Rotor(
        wiring=ROTORS_DATA["I"]['wiring'], notch_position=ROTORS_DATA["I"]['notch'],
        initial_position='a'
    )
    r2 = Rotor(
        wiring=ROTORS_DATA["II"]['wiring'], notch_position=ROTORS_DATA["II"]['notch'],
        initial_position='a'
    )
    r3 = Rotor(
        wiring=ROTORS_DATA["III"]['wiring'], notch_position=ROTORS_DATA["III"]['notch'],
        initial_position='a'
    )
    ref = Reflector(
        REFLECTORS_DATA["B"]
    )
    pb = Plugboard()

    enigma = Enigma(rotor1=r1, rotor2=r2, rotor3=r3, reflector=ref, plugboard=pb)

    encrypted = enigma.encrypt("AAAAA")

    assert encrypted == "BDZGO"


def test_double_stepping():
    r1 = Rotor(wiring=ROTORS_DATA["I"]["wiring"], notch_position=ROTORS_DATA["I"]["notch"], initial_position="A")
    r2 = Rotor(wiring=ROTORS_DATA["II"]["wiring"], notch_position=ROTORS_DATA["II"]["notch"], initial_position="D")
    r3 = Rotor(wiring=ROTORS_DATA["III"]["wiring"], notch_position=ROTORS_DATA["III"]["notch"], initial_position="U")
    ref = Reflector(REFLECTORS_DATA["B"])
    pb = Plugboard()

    enigma = Enigma(r1, r2, r3, ref, pb)

    encrypted = enigma.encrypt("AAAAA")

    assert encrypted == "EQIBM"


def test_plugboard_swap():
    r1 = Rotor(wiring=ROTORS_DATA["I"]["wiring"], notch_position=ROTORS_DATA["I"]["notch"], initial_position="A")
    r2 = Rotor(wiring=ROTORS_DATA["II"]["wiring"], notch_position=ROTORS_DATA["II"]["notch"], initial_position="A")
    r3 = Rotor(wiring=ROTORS_DATA["III"]["wiring"], notch_position=ROTORS_DATA["III"]["notch"], initial_position="A")
    ref = Reflector(REFLECTORS_DATA["B"])
    pb = Plugboard('AB')

    enigma = Enigma(r1, r2, r3, ref, pb)

    encrypted = enigma.encrypt("AAAAA")

    assert encrypted == "BJLCS"


def test_decryption_symmetry():
    # Konfiguracja
    r1 = Rotor(wiring=ROTORS_DATA["I"]["wiring"], notch_position=ROTORS_DATA["I"]["notch"], initial_position="G")
    r2 = Rotor(wiring=ROTORS_DATA["II"]["wiring"], notch_position=ROTORS_DATA["II"]["notch"], initial_position="H")
    r3 = Rotor(wiring=ROTORS_DATA["III"]["wiring"], notch_position=ROTORS_DATA["III"]["notch"], initial_position="K")
    ref = Reflector(REFLECTORS_DATA["B"])
    pb = Plugboard("AB CD EF")

    enigma = Enigma(r1, r2, r3, ref, pb)

    message = "TAJNEHASLO"

    # 1. Szyfrowanie
    cipher_text = enigma.encrypt(message)

    # 2. Resetujemy maszynę do tej samej pozycji startowej!
    r1.set_current_position(char_to_int('G'))
    r2.set_current_position(char_to_int('H'))
    r3.set_current_position(char_to_int('K'))

    # 3. Odszyfrowywanie (ponowne wrzucenie szyfrogramu)
    decrypted_text = enigma.encrypt(cipher_text)

    # Assert
    assert decrypted_text == message
