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
    rotor1 = Rotor(name='I', initial_position='a')
    rotor2 = Rotor(name='II', initial_position='a')
    rotor3 = Rotor(name='III', initial_position='a')

    reflector = Reflector(name='B')

    plugborad = Plugboard()

    enigma = Enigma(rotor1, rotor2, rotor3, reflector, plugborad)

    assert enigma.rotor1 == rotor1
    assert enigma.rotor2 == rotor2
    assert enigma.rotor3 == rotor3
    assert enigma.reflector == reflector
    assert enigma.plugboard == plugborad


def test_enigma_create_missing_component():
    rotor1 = Rotor(name='I', initial_position='a')
    rotor2 = Rotor(name='II', initial_position='a')
    rotor3 = Rotor(name='III', initial_position='a')

    reflector = Reflector(name='B')

    with pytest.raises(TypeError):
        Enigma(rotor1, rotor2, rotor3, reflector)


# SETTERS
def test_enigma_set_rotor():
    rotor1 = Rotor(name='I', initial_position='a')
    rotor2 = Rotor(name='II', initial_position='a')
    rotor3 = Rotor(name='III', initial_position='a')
    rotor4 = Rotor(name='IV', initial_position='a')

    reflector = Reflector(name='B')

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
    rotor1 = Rotor(name='I', initial_position='a')
    rotor2 = Rotor(name='II', initial_position='a')
    rotor3 = Rotor(name='III', initial_position='a')

    reflector = Reflector(name='B')
    reflector2 = Reflector(name='C')

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
    rotor1 = Rotor(name='I', initial_position='a')
    rotor2 = Rotor(name='II', initial_position='a')
    rotor3 = Rotor(name='III', initial_position='a')

    reflector = Reflector(name='B')

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
    rotor1 = Rotor(name='I', initial_position='a')
    rotor2 = Rotor(name='II', initial_position='a')
    rotor3 = Rotor(name='III', initial_position='v')

    reflector = Reflector(name='B')

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
    rotor1 = Rotor(name='I', initial_position='a')
    rotor2 = Rotor(name='II', initial_position='e')
    rotor3 = Rotor(name='III', initial_position='a')

    reflector = Reflector(name='B')

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
    rotor1 = Rotor(name='I', initial_position='q')
    rotor2 = Rotor(name='II', initial_position='a')
    rotor3 = Rotor(name='III', initial_position='a')

    reflector = Reflector(name='B')

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
    rotor1 = Rotor(name='I', initial_position='a')
    rotor2 = Rotor(name='II', initial_position='d')
    rotor3 = Rotor(name='III', initial_position='u')

    reflector = Reflector(name='B')

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
    r1 = Rotor(name='I', initial_position='a')
    r2 = Rotor(name='II', initial_position='a')
    r3 = Rotor(name='III', initial_position='a')

    ref = Reflector(name='B')

    pb = Plugboard()

    enigma = Enigma(rotor1=r1, rotor2=r2, rotor3=r3, reflector=ref, plugboard=pb)

    encrypted = enigma.encrypt("AAAAA")

    assert encrypted == "BDZGO"


def test_double_stepping():
    r1 = Rotor(name='I', initial_position='a')
    r2 = Rotor(name='II', initial_position='d')
    r3 = Rotor(name='III', initial_position='u')

    ref = Reflector(name='B')

    pb = Plugboard()

    enigma = Enigma(r1, r2, r3, ref, pb)

    encrypted = enigma.encrypt("AAAAA")

    assert encrypted == "EQIBM"


def test_plugboard_swap():
    r1 = Rotor(name='I', initial_position='a')
    r2 = Rotor(name='II', initial_position='a')
    r3 = Rotor(name='III', initial_position='a')

    ref = Reflector(name='B')

    pb = Plugboard('ab')

    enigma = Enigma(r1, r2, r3, ref, pb)

    encrypted = enigma.encrypt("AAAAA")

    assert encrypted == "BJLCS"


def test_decryption_symmetry():
    r1 = Rotor(name='I', initial_position='g')
    r2 = Rotor(name='II', initial_position='h')
    r3 = Rotor(name='III', initial_position='k')

    ref = Reflector(name='B')

    pb = Plugboard("AB CD EF")

    enigma = Enigma(r1, r2, r3, ref, pb)

    message = "TAJNEHASLO"
    cipher_text = enigma.encrypt(message)

    r1.set_current_position(char_to_int('G'))
    r2.set_current_position(char_to_int('H'))
    r3.set_current_position(char_to_int('K'))

    decrypted_text = enigma.encrypt(cipher_text)

    assert decrypted_text == message


def test_enigma_encrypt_ring_setting():
    r1 = Rotor(name='I', initial_position='a', ring_setting='d')
    r2 = Rotor(name='II', initial_position='a', ring_setting='f')
    r3 = Rotor(name='III', initial_position='a', ring_setting='g')

    ref = Reflector(name='B')

    pb = Plugboard()

    enigma = Enigma(r1, r2, r3, ref, pb)

    encrypted = enigma.encrypt("AAAAA")

    assert encrypted == "XNEIU"


# rotor1 = Rotor(
#     wiring=ROTORS_DATA["I"]['wiring'], notch_position=ROTORS_DATA["I"]['notch'],
#     initial_position='a'
# )
# rotor2 = Rotor(
#     wiring=ROTORS_DATA["II"]['wiring'], notch_position=ROTORS_DATA["II"]['notch'],
#     initial_position='a'
# )
# rotor3 = Rotor(
#     wiring=ROTORS_DATA["III"]['wiring'], notch_position=ROTORS_DATA["III"]['notch'],
#     initial_position='a'
# )

# reflector = Reflector(
#     REFLECTORS_DATA["B"]
# )

# plugborad = Plugboard()

# enigma = Enigma(rotor1, rotor2, rotor3, reflector, plugborad)

# enigma.save_enigma_settings()
