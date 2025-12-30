from components import (
    Rotor, Reflector, Plugboard,
    RotorConfigurationError,
    ReflectorConfigurationError,
    PlugboardConfigurationError,
)
from utils import char_to_int, int_to_char
import json


class MalformedDataError(Exception):
    pass


class InvalidComponentError(Exception):
    pass


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

    def set_rotor1(self, new_rotor: Rotor) -> Rotor:
        self._rotor1 = new_rotor
        return self._rotor1

    def set_rotor2(self, new_rotor: Rotor) -> Rotor:
        self._rotor2 = new_rotor
        return self._rotor2

    def set_rotor3(self, new_rotor: Rotor) -> Rotor:
        self._rotor3 = new_rotor
        return self._rotor3

    def set_plugboard(self, new_plugboard: Plugboard) -> Plugboard:
        self._plugboard = new_plugboard
        return self._plugboard

    def set_reflector(self, new_reflector: Reflector) -> Reflector:
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
        text = text.upper()
        encrypted_text = ''
        for char in text:
            if char.isalpha() and char.isascii():
                self.step()
                signal = char_to_int(char)
                signal = self.plugboard.connections[signal]
                signal = self.rotor3.encrypt_forward(signal)
                signal = self.rotor2.encrypt_forward(signal)
                signal = self.rotor1.encrypt_forward(signal)
                signal = self.reflector.wiring[signal]
                signal = self.rotor1.encrypt_backward(signal)
                signal = self.rotor2.encrypt_backward(signal)
                signal = self.rotor3.encrypt_backward(signal)
                signal = self.plugboard.connections[signal]
                encrypted_text += int_to_char(signal)
        return encrypted_text

    def save_enigma_settings(self, file_handle):
        settings = {
            'rotor1': {
                'name': self.rotor1.name,
                'initial_position': self.rotor1.current_position,
                'ring_setting': self.rotor1.ring_setting
            },

            'rotor2': {
                'name': self.rotor2.name,
                'initial_position': self.rotor2.current_position,
                'ring_setting': self.rotor2.ring_setting
            },

            'rotor3': {
                'name': self.rotor3.name,
                'initial_position': self.rotor3.current_position,
                'ring_setting': self.rotor3.ring_setting
            },

            'reflector': {
                'name': self.reflector.name
            },

            'plugboard': {
                'connections': self.plugboard.connections_as_str
            }
        }
        json.dump(settings, file_handle, indent=4)

    def load_enigma_settings(self, file_handle):
        try:
            data = json.load(file_handle)
        except json.JSONDecodeError as e:
            raise MalformedDataError("File is not json file") from e
        try:
            new_rotor1 = Rotor(
                name=data['rotor1']['name'],
                initial_position=data['rotor1']['initial_position'],
                ring_setting=data['rotor1']["ring_setting"]
            )
            new_rotor2 = Rotor(
                name=data['rotor2']['name'],
                initial_position=data['rotor2']['initial_position'],
                ring_setting=data['rotor2']["ring_setting"]
            )
            new_rotor3 = Rotor(
                name=data['rotor3']['name'],
                initial_position=data['rotor3']['initial_position'],
                ring_setting=data['rotor3']["ring_setting"]
            )

            new_reflector = Reflector(data['reflector']['name'])
            new_plugboard = Plugboard(data['plugboard']['connections'])
        except KeyError as e:
            raise MalformedDataError("Missing key in file") from e
        except (
            RotorConfigurationError, PlugboardConfigurationError,
            ReflectorConfigurationError
        ) as e:
            raise InvalidComponentError("Invalid data detected during settings loading") from e

        self.set_rotor1(new_rotor1)
        self.set_rotor2(new_rotor2)
        self.set_rotor3(new_rotor3)
        self.set_plugboard(new_plugboard)
        self.set_reflector(new_reflector)
