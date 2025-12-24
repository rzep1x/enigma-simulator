from utils import char_to_int


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


class Rotor:
    def __init__(self, notch_position: str, wiring: str, initial_position: str, ring_setting: str = 'A'):

        # Validation for notch position
        if not isinstance(notch_position, str) or len(notch_position) != 1:
            raise RotorConfigurationNotchPositionError
        if not notch_position.isascii() or not notch_position.isalpha():
            # .isalpha() checks for special characters
            # .isascii() checks for non ascii characters like ą,ł,ć etc
            raise RotorConfigurationNotchPositionError

        # Validation for wiring
        if not isinstance(wiring, str) or len(wiring) != 26:
            raise RotorConfigurationWiringError
        if not wiring.isalpha() or not wiring.isascii():
            raise RotorConfigurationWiringError

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

        # Convert input strings to internal integer representation (0-25)
        self._notch_position = char_to_int(notch_position)
        self._wiring = [char_to_int(letter) for letter in wiring]

        # Create reversed wiring list
        self._reveresed_wiring = [0] * len(self._wiring)
        for index, value in enumerate(self._wiring):
            self._reveresed_wiring[value] = index

        self._initial_position = char_to_int(initial_position)
        self._ring_setting = char_to_int(ring_setting)
        self._current_position = self.initial_position

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
        if not isinstance(new_value, int):
            raise RotorConfigurationCurrentPositionError
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

    def step(self):
        pass

    def encrypt_forward(self):
        pass

    def encrypt_backward(self):
        pass


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
                # TODO CUSTOM ERROR
                raise ValueError
            if not pair.isalpha() or not pair.isascii():
                # TODO CUSTOM ERROR
                raise ValueError
            char1 = char_to_int(pair[0])
            char2 = char_to_int(pair[1])
            if char1 in used_chars or char2 in used_chars:
                # TODO CUSTOM EROOR
                raise ValueError

            used_chars.add(char1)
            used_chars.add(char2)

            self._connections[char1] = char2
            self._connections[char2] = char1

    @property
    def connections(self):
        return self._connections
