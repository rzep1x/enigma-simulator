from components import Rotor, Reflector, Plugboard


class Enigma:
    def __init__(self, rotor1: Rotor, rotor2: Rotor, rotor3: Rotor, reflector: Reflector, plugboard: Plugboard):
        self._rotor1 = rotor1
        self._rotor2 = rotor2
        self._rotor3 = rotor3
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

    def set_rotor1(self, new_rotor):
        self._rotor1 = new_rotor
        return self._rotor1

    def set_rotor2(self, new_rotor):
        self._rotor2 = new_rotor
        return self._rotor2

    def set_rotor3(self, new_rotor):
        self._rotor3 = new_rotor
        return self._rotor3

    def set_plugboard(self, new_plugboard):
        self._plugboard = new_plugboard
        return self._plugboard

    def set_reflector(self, new_reflector):
        self._reflector = new_reflector
        return self._reflector

    def step(self):
        if self._rotor1.is_at_notch():
            if self._rotor2.is_at_notch():
                self._rotor2.step()
                self._rotor3.step()
            else:
                self._rotor2.step()
        elif self._rotor2.is_at_notch():
            self._rotor2.step()
            self._rotor3.step()

        self._rotor1.step()


