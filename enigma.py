from components import Rotor, Reflector, Plugboard
from config import config

class Enigma:
    def __init__(self, rotor1: Rotor, rotor2: Rotor, rotor3: Rotor, reflector: Reflector, plugboard: Plugboard):
        self._rotor1 = rotor1
        self._rotor2 = rotor2
        self._rotor2 = rotor3
        self._reflector = reflector
        self._plugboard = plugboard

    @property
    def rotor1(self):
        return self._rotor1

    @property
    def rotor2(self):
        return self._rotor2

    @property
    def rotor3(self):
        return self._rotor3

    @property
    def reflector(self):
        return self._reflector

    @property
    def plugboard(self):
        return self._plugboard
