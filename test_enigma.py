from enigma import Enigma
from components import Rotor, Plugboard, Reflector
import pytest
from utils import char_to_int
from io import StringIO

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
    rotor1 = Rotor(name='I', initial_position=0)
    rotor2 = Rotor(name='II', initial_position=0)
    rotor3 = Rotor(name='III', initial_position=0)

    reflector = Reflector(name='B')

    plugboard = Plugboard()

    enigma = Enigma(rotor1, rotor2, rotor3, reflector, plugboard)

    assert enigma.rotor1 == rotor1
    assert enigma.rotor2 == rotor2
    assert enigma.rotor3 == rotor3
    assert enigma.reflector == reflector
    assert enigma.plugboard == plugboard


def test_enigma_create_missing_component():
    rotor1 = Rotor(name='I', initial_position=0)
    rotor2 = Rotor(name='II', initial_position=0)
    rotor3 = Rotor(name='III', initial_position=0)

    reflector = Reflector(name='B')

    with pytest.raises(TypeError):
        Enigma(rotor1, rotor2, rotor3, reflector)


# SETTERS
def test_enigma_set_rotor():
    rotor1 = Rotor(name='I', initial_position=0)
    rotor2 = Rotor(name='II', initial_position=0)
    rotor3 = Rotor(name='III', initial_position=0)
    rotor4 = Rotor(name='IV', initial_position=0)

    reflector = Reflector(name='B')

    plugboard = Plugboard()

    enigma = Enigma(rotor1, rotor2, rotor3, reflector, plugboard)

    assert enigma.rotor1 == rotor1
    assert enigma.rotor2 == rotor2
    assert enigma.rotor3 == rotor3
    assert enigma.reflector == reflector
    assert enigma.plugboard == plugboard

    enigma.set_rotor1(rotor4)
    enigma.set_rotor2(rotor1)
    assert enigma.rotor1 == rotor4
    assert enigma.rotor2 == rotor1
    assert enigma.rotor3 == rotor3
    assert enigma.reflector == reflector
    assert enigma.plugboard == plugboard


def test_enigma_reflector_setter():
    rotor1 = Rotor(name='I', initial_position=0)
    rotor2 = Rotor(name='II', initial_position=0)
    rotor3 = Rotor(name='III', initial_position=0)

    reflector = Reflector(name='B')
    reflector2 = Reflector(name='C')

    plugboard = Plugboard()
    enigma = Enigma(rotor1, rotor2, rotor3, reflector, plugboard)

    assert enigma.rotor1 == rotor1
    assert enigma.rotor2 == rotor2
    assert enigma.rotor3 == rotor3
    assert enigma.reflector == reflector
    assert enigma.plugboard == plugboard
    enigma.set_reflector(reflector2)
    assert enigma.reflector == reflector2


def test_enigma_step_nothing_on_notch():
    rotor1 = Rotor(name='I', initial_position=0)
    rotor2 = Rotor(name='II', initial_position=0)
    rotor3 = Rotor(name='III', initial_position=0)

    reflector = Reflector(name='B')

    plugboard = Plugboard()
    enigma = Enigma(rotor1, rotor2, rotor3, reflector, plugboard)
    assert enigma.rotor1.current_position == 0
    assert enigma.rotor2.current_position == 0
    assert enigma.rotor3.current_position == 0
    enigma.step()
    assert enigma.rotor1.current_position == 0
    assert enigma.rotor2.current_position == 0
    assert enigma.rotor3.current_position == 1


def test_enigma_step_first_rotor_on_notch():
    rotor1 = Rotor(name='I', initial_position=0)
    rotor2 = Rotor(name='II', initial_position=0)
    rotor3 = Rotor(name='III', initial_position=21)

    reflector = Reflector(name='B')

    plugboard = Plugboard()
    enigma = Enigma(rotor1, rotor2, rotor3, reflector, plugboard)
    assert enigma.rotor1.current_position == 0
    assert enigma.rotor2.current_position == 0
    assert enigma.rotor3.current_position == 21
    enigma.step()
    assert enigma.rotor1.current_position == 0
    assert enigma.rotor2.current_position == 1
    assert enigma.rotor3.current_position == 22


def test_enigma_step_second_rotor_on_notch():
    rotor1 = Rotor(name='I', initial_position=0)
    rotor2 = Rotor(name='II', initial_position=4)
    rotor3 = Rotor(name='III', initial_position=0)

    reflector = Reflector(name='B')

    plugboard = Plugboard()

    enigma = Enigma(rotor1, rotor2, rotor3, reflector, plugboard)
    assert enigma.rotor1.current_position == 0
    assert enigma.rotor2.current_position == 4
    assert enigma.rotor3.current_position == 0
    enigma.step()
    assert enigma.rotor1.current_position == 1
    assert enigma.rotor2.current_position == 5
    assert enigma.rotor3.current_position == 1


def test_enigma_step_third_rotor_on_notch():
    rotor1 = Rotor(name='I', initial_position=16)
    rotor2 = Rotor(name='II', initial_position=0)
    rotor3 = Rotor(name='III', initial_position=0)

    reflector = Reflector(name='B')

    plugboard = Plugboard()

    enigma = Enigma(rotor1, rotor2, rotor3, reflector, plugboard)
    assert enigma.rotor1.current_position == 16
    assert enigma.rotor2.current_position == 0
    assert enigma.rotor3.current_position == 0
    enigma.step()
    assert enigma.rotor1.current_position == 16
    assert enigma.rotor2.current_position == 0
    assert enigma.rotor3.current_position == 1


def test_enigma_step_double_step():
    rotor1 = Rotor(name='I', initial_position=0)
    rotor2 = Rotor(name='II', initial_position=3)
    rotor3 = Rotor(name='III', initial_position=20)

    reflector = Reflector(name='B')

    plugboard = Plugboard()

    enigma = Enigma(rotor1, rotor2, rotor3, reflector, plugboard)
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
    r1 = Rotor(name='I', initial_position=0)
    r2 = Rotor(name='II', initial_position=0)
    r3 = Rotor(name='III', initial_position=0)

    ref = Reflector(name='B')

    pb = Plugboard()

    enigma = Enigma(rotor1=r1, rotor2=r2, rotor3=r3, reflector=ref, plugboard=pb)

    encrypted = enigma.encrypt("AAAAA")

    assert encrypted == "BDZGO"


def test_double_stepping():
    r1 = Rotor(name='I', initial_position=0)
    r2 = Rotor(name='II', initial_position=4)
    r3 = Rotor(name='III', initial_position=20)

    ref = Reflector(name='B')

    pb = Plugboard()

    enigma = Enigma(r1, r2, r3, ref, pb)

    encrypted = enigma.encrypt("AAAAA")

    assert encrypted == "BRNCO"


def test_plugboard_swap():
    r1 = Rotor(name='I', initial_position=0)
    r2 = Rotor(name='II', initial_position=0)
    r3 = Rotor(name='III', initial_position=0)

    ref = Reflector(name='B')

    pb = Plugboard('ab')

    enigma = Enigma(r1, r2, r3, ref, pb)

    encrypted = enigma.encrypt("AAAAA")

    assert encrypted == "BJLCS"


def test_decryption_symmetry():
    r1 = Rotor(name='I', initial_position=6)
    r2 = Rotor(name='II', initial_position=7)
    r3 = Rotor(name='III', initial_position=10)

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
    r1 = Rotor(name='I', initial_position=0, ring_setting=3)
    r2 = Rotor(name='II', initial_position=0, ring_setting=5)
    r3 = Rotor(name='III', initial_position=0, ring_setting=6)

    ref = Reflector(name='B')

    pb = Plugboard()

    enigma = Enigma(r1, r2, r3, ref, pb)

    encrypted = enigma.encrypt("AAAAA")

    assert encrypted == "XNEIU"


def test_encrypt_ignores_special_characters_nad_numbers():
    r1 = Rotor(name='I', initial_position=0, ring_setting=0)
    r2 = Rotor(name='II', initial_position=0, ring_setting=0)
    r3 = Rotor(name='III', initial_position=0, ring_setting=0)
    ref = Reflector(name='B')
    pb = Plugboard()
    enigma = Enigma(r1, r2, r3, ref, pb)

    encrpted_text = enigma.encrypt("AAA !ąa.  a@#")
    assert encrpted_text == "BDZGO"


def test_encrypt_lowercase():
    r1 = Rotor(name='I', initial_position=0, ring_setting=0)
    r2 = Rotor(name='II', initial_position=0, ring_setting=0)
    r3 = Rotor(name='III', initial_position=0, ring_setting=0)
    ref = Reflector(name='B')
    pb = Plugboard()
    enigma = Enigma(r1, r2, r3, ref, pb)

    assert enigma.encrypt("aaaaa") == "BDZGO"


def test_enctpy_empty_str():
    r1 = Rotor(name='I', initial_position=0, ring_setting=0)
    r2 = Rotor(name='II', initial_position=0, ring_setting=0)
    r3 = Rotor(name='III', initial_position=0, ring_setting=0)
    ref = Reflector(name='B')
    pb = Plugboard()
    enigma = Enigma(r1, r2, r3, ref, pb)
    assert enigma.encrypt('') == ''


def test_enigma_save_enigma_settings():
    rotor1 = Rotor(name='I', initial_position=16)
    rotor2 = Rotor(name='II', initial_position=0)
    rotor3 = Rotor(name='III', initial_position=0)
    reflector = Reflector(name='B')
    plugboard = Plugboard('AB CD')
    enigma = Enigma(rotor1, rotor2, rotor3, reflector, plugboard)
    file_handle = StringIO()

    enigma.save_enigma_settings(file_handle)
    output_content = file_handle.getvalue()
    assert '"name": "I"' in output_content
    assert '"connections": "AB CD"' in output_content


def test_load_enigma_settings_from_stringio():
    rotor1 = Rotor(name='I', initial_position=16)
    rotor2 = Rotor(name='II', initial_position=0)
    rotor3 = Rotor(name='III', initial_position=0)
    reflector = Reflector(name='B')
    plugboard = Plugboard('AB CD')
    enigma = Enigma(rotor1, rotor2, rotor3, reflector, plugboard)
    json_data = """
    {
        "rotor1": {"name": "V", "initial_position": 25, "ring_setting": 7},
        "rotor2": {"name": "IV", "initial_position": 12, "ring_setting": 12},
        "rotor3": {"name": "III", "initial_position": 16, "ring_setting": 11},
        "reflector": {"name": "C"},
        "plugboard": {"connections": "XY WF"}
    }
    """

    file_handle = StringIO(json_data)

    enigma.load_enigma_settings(file_handle)

    assert enigma.rotor1.name == "V"
    assert enigma.reflector.name == "C"


# rotor1 = Rotor(name='I', initial_position='a')
# rotor2 = Rotor(name='II', initial_position='a')
# rotor3 = Rotor(name='III', initial_position='a')

# reflector = Reflector(name='B')

# Plugboard = Plugboard('ab')

# enigma = Enigma(rotor1, rotor2, rotor3, reflector, Plugboard)

# enigma.save_enigma_settings()
