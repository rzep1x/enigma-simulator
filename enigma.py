from components import Rotor, Reflector, Plugboard
from utils import char_to_int, int_to_char
import json


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
        if self._rotor3.is_at_notch():
            if self._rotor2.is_at_notch():
                self._rotor2.step()
                self._rotor1.step()
            else:
                self._rotor2.step()
        elif self._rotor2.is_at_notch():
            self._rotor2.step()
            self._rotor1.step()
        self._rotor3.step()

    def encrypt(self, text: str) -> str:
        clean_text = text.replace(" ", "").upper()
        if not clean_text.isascii() or not clean_text.isalpha():
            # TODO CUSTOM ERROR
            raise ValueError
        num_text = [char_to_int(char) for char in clean_text]
        encyrpted_text = ''
        for num in num_text:
            self.step()
            signal = num
            signal = self.plugboard.connections[signal]
            signal = self.rotor3.encrypt_forward(signal)
            signal = self.rotor2.encrypt_forward(signal)
            signal = self.rotor1.encrypt_forward(signal)
            signal = self.reflector.wiring[signal]
            signal = self.rotor1.encrypt_backward(signal)
            signal = self.rotor2.encrypt_backward(signal)
            signal = self.rotor3.encrypt_backward(signal)
            signal = self.plugboard.connections[signal]
            encyrpted_text += int_to_char(signal)
        return encyrpted_text

    def save_enigma_settings(self):
        settings = {
            'rotor1': {
                'wiring': ''.join([int_to_char(letter) for letter in self.rotor1.wiring]),
                'initial_position': int_to_char(self.rotor1.initial_position),
                'notch_position': int_to_char(self.rotor1.notch_position),
                'ring_setting': int_to_char(self.rotor1.ring_setting),
            },

            'rotor2': {
                'wiring': ''.join([int_to_char(letter) for letter in self.rotor2.wiring]),
                'initial_position': int_to_char(self.rotor2.initial_position),
                'notch_position': int_to_char(self.rotor2.notch_position),
                'ring_setting': int_to_char(self.rotor2.ring_setting),
            },

            'rotor3': {
                'wiring': ''.join([int_to_char(letter) for letter in self.rotor3.wiring]),
                'initial_position': int_to_char(self.rotor3.initial_position),
                'notch_position': int_to_char(self.rotor3.notch_position),
                'ring_setting': int_to_char(self.rotor3.ring_setting),
            },

            'reflector': {
                'wiring': ''.join([int_to_char(letter) for letter in self.reflector.wiring])
            },

            'plugboard': {
                'connections': ''.join([int_to_char(letter) for letter in self.plugboard.connections])
            }
        }

        with open('settings.json', 'w') as file_handle:
            json.dump(settings, file_handle, indent=4)
