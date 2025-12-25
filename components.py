from utils import char_to_int
from config import ROTORS_DATA


class RotorConfigurationWiringError(Exception):
    pass


class RotorConfigurationNotchPositionError(Exception):
    pass


class RotorConfigurationInitialPositionError(Exception):
    pass


class RotorConfigurationRingSettingError(Exception):
    pass


class RotorConfigurationCurrentPositionError(Exception):
    pass


class PlugboradConfigurationError(Exception):
    pass


class Rotor:
    def __init__(self, name: str, initial_position: str, ring_setting: str = 'A'):

        # Validation for name
        if name not in ROTORS_DATA:
            # TODO custom error
            raise ValueError

        # Validation for initial postion
        if not isinstance(initial_position, str) or len(initial_position) != 1:
            raise RotorConfigurationInitialPositionError
        if not initial_position.isalpha() or not initial_position.isascii():
            raise RotorConfigurationInitialPositionError

        # Validation for ring_setting
        if not isinstance(ring_setting, str) or len(ring_setting) != 1:
            raise RotorConfigurationRingSettingError
        if not ring_setting.isalpha() or not ring_setting.isascii():
            raise RotorConfigurationRingSettingError

        self._notch_position = char_to_int(ROTORS_DATA[name]['notch'])
        self._wiring = [char_to_int(letter) for letter in ROTORS_DATA[name]['wiring']]

        # Create reversed wiring list
        self._reveresed_wiring = [0] * len(self._wiring)
        for index, value in enumerate(self._wiring):
            self._reveresed_wiring[value] = index

        self._initial_position = char_to_int(initial_position)
        self._ring_setting = char_to_int(ring_setting)
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
        return self._reveresed_wiring

    @property
    def initial_position(self):
        return self._initial_position

    @property
    def current_position(self):
        return self._current_position

    @property
    def ring_setting(self):
        return self._ring_setting

    def set_current_position(self, new_value: int):
        """
        sets new position of my rotor
        """
        self._current_position = new_value % 26
        return self.current_position

    def set_initial_position(self, new_value: int):
        if not isinstance(new_value, int):
            raise RotorConfigurationInitialPositionError
        self._initial_position = new_value % 26
        self._current_position = self.initial_position
        return self.initial_position

    def set_ring_setting(self, new_value: int):
        if not isinstance(new_value, int):
            raise RotorConfigurationRingSettingError
        self._ring_setting = new_value % 26
        return self.ring_setting

    def step(self) -> int:
        self.set_current_position(self._current_position + 1)
        return self.current_position

    def is_at_notch(self) -> bool:
        return self._current_position == self._notch_position

    def encrypt_forward(self, input_index):
        shift = self.current_position - self.ring_setting
        index_in = (input_index + shift) % 26
        mapped_index = self._wiring[index_in]
        index_out = (mapped_index - shift) % 26
        return index_out

    def encrypt_backward(self, input_index):
        shift = self.current_position - self.ring_setting
        index_in = (input_index + shift) % 26
        mapped_index = self._reveresed_wiring[index_in]
        index_out = (mapped_index - shift) % 26
        return index_out


class Reflector:
    """
    Class Reflector. Contains attributes:
    :param wiring: reflectors wiring
    :type name: str
    """
    def __init__(self, wiring: str):
        self._wiring = [char_to_int(letter) for letter in wiring]

    @property
    def wiring(self):
        return self._wiring


class Plugboard:
    def __init__(self, connections=''):
        used_chars = set()
        self._connections = [num for num in range(26)]
        if not connections:
            return
        pairs = connections.upper().split()
        for pair in pairs:
            if len(pair) != 2:
                raise PlugboradConfigurationError
            if not pair.isalpha() or not pair.isascii():
                raise PlugboradConfigurationError
            char1 = char_to_int(pair[0])
            char2 = char_to_int(pair[1])
            if char1 in used_chars or char2 in used_chars:
                raise PlugboradConfigurationError

            used_chars.add(char1)
            used_chars.add(char2)

            self._connections[char1] = char2
            self._connections[char2] = char1

    @property
    def connections(self):
        return self._connections
