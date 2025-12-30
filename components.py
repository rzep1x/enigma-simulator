from utils import char_to_int
from config import ROTORS_DATA, REFLECTORS_DATA


class RotorConfigurationError(Exception):
    pass


class PlugboardConfigurationError(Exception):
    pass


class ReflectorConfigurationError(Exception):
    pass


class Rotor:
    def __init__(self, name: str, initial_position: int, ring_setting: int = 0):

        # Validation for name
        if name not in ROTORS_DATA:
            raise RotorConfigurationError("Unknown rotor: {name}")

        # Validation for initial postion
        if not isinstance(initial_position, int):
            raise RotorConfigurationError("Initial position must be an integer")

        # Validation for ring_setting
        if not isinstance(ring_setting, int):
            raise RotorConfigurationError("Ring setting must be an integer")

        self._name = name
        self._notch_position = char_to_int(ROTORS_DATA[name]['notch'])
        self._wiring = [char_to_int(letter) for letter in ROTORS_DATA[name]['wiring']]

        # Create reversed wiring list
        self._reversed_wiring = [0] * len(self._wiring)
        for index, value in enumerate(self._wiring):
            self._reversed_wiring[value] = index

        self._initial_position = initial_position
        self._ring_setting = ring_setting
        self._current_position = self.initial_position

    @property
    def name(self):
        return self._name

    @property
    def notch_position(self):
        return self._notch_position

    @property
    def wiring(self):
        return self._wiring

    @property
    def reversed_wiring(self):
        return self._reversed_wiring

    @property
    def initial_position(self):
        return self._initial_position

    @property
    def current_position(self):
        return self._current_position

    @property
    def ring_setting(self):
        return self._ring_setting

    def set_current_position(self, new_value: int) -> int:
        """
        sets new position of my rotor
        """
        self._current_position = new_value % 26
        return self.current_position

    def set_initial_position(self, new_value: int) -> int:
        if not isinstance(new_value, int):
            raise RotorConfigurationError("New initial position must be integer")
        self._initial_position = new_value % 26
        self._current_position = self.initial_position
        return self.initial_position

    def set_ring_setting(self, new_value: int) -> int:
        if not isinstance(new_value, int):
            raise RotorConfigurationError("New ring setting must be integer")
        self._ring_setting = new_value % 26
        return self.ring_setting

    def step(self) -> int:
        self.set_current_position(self._current_position + 1)
        return self.current_position

    def is_at_notch(self) -> bool:
        return self._current_position == self._notch_position

    def encrypt_forward(self, input_index) -> int:
        shift = self.current_position - self.ring_setting
        index_in = (input_index + shift) % 26
        mapped_index = self._wiring[index_in]
        index_out = (mapped_index - shift) % 26
        return index_out

    def encrypt_backward(self, input_index) -> int:
        shift = self.current_position - self.ring_setting
        index_in = (input_index + shift) % 26
        mapped_index = self._reversed_wiring[index_in]
        index_out = (mapped_index - shift) % 26
        return index_out


class Reflector:
    def __init__(self, name: str):
        if name not in REFLECTORS_DATA:
            raise ReflectorConfigurationError("Unknown reflector")
        self._name = name
        self._wiring = [char_to_int(letter) for letter in REFLECTORS_DATA[name]]

    @property
    def name(self):
        return self._name

    @property
    def wiring(self):
        return self._wiring


class Plugboard:
    def __init__(self, connections=''):
        used_chars = set()
        self._connections = [num for num in range(26)]
        self._connections_as_str = connections.upper()
        if not connections:
            return
        pairs = connections.upper().split()
        for pair in pairs:
            if len(pair) != 2:
                raise PlugboardConfigurationError(
                    "Invalid plugboard format: pairs of letters to be swapped expected (e.g 'ab cd ef')"
                )
            if not pair.isalpha() or not pair.isascii() or pair[0] == pair[1]:
                raise PlugboardConfigurationError(
                    "Invalid plugboard format: pairs of letters to be swapped expected (e.g 'ab cd ef')"
                )
            char1 = char_to_int(pair[0])
            char2 = char_to_int(pair[1])
            if char1 in used_chars or char2 in used_chars:
                raise PlugboardConfigurationError(
                    "Pair of letters to be swapped need to be unique"
                )
            used_chars.add(char1)
            used_chars.add(char2)

            self._connections[char1] = char2
            self._connections[char2] = char1

    @property
    def connections(self):
        return self._connections

    @property
    def connections_as_str(self):
        return self._connections_as_str
