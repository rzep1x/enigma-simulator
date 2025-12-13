from utils import char_to_int


class RotorConfigarationWiringError(Exception):
    pass


class RotorConfigurationNotchPositionError(Exception):
    pass


class RotorConfigurationInitialPositionError(Exception):
    pass


class RotorConfigurationRingSettingError(Exception):
    pass


class Rotor:
    """
    Class Rotor. Contains attributes:
    :param notch_position: rotors notch positiob
    :type name: int

    :param wiring: rotors wiring list
    :type wiring: str

    :param reversed_wiring: reversed wiring
    :type wiring: str
    """
    def __init__(self, notch_position: chr, wiring: str, initial_poition: chr, ring_setting: chr = 'A'):
        # .isalpha() function checks if my string is from alphabet

        if not isinstance(notch_position, str) or len(notch_position) != 1 or not notch_position.isalpha():
            # raising custom error when notch_postition is wrong
            raise RotorConfigurationNotchPositionError
        if not isinstance(wiring, str) or len(wiring) != 26 or not wiring.isalpha():
            # raising error wiring is wrong
            raise RotorConfigarationWiringError
        if not isinstance(initial_poition, str) or len(initial_poition) != 1 or not initial_poition.isalpha():
            # raising error when initial position is wrong
            raise RotorConfigurationInitialPositionError
        if not isinstance(ring_setting, str) or len(ring_setting) != 1 or not ring_setting.isalpha():
            # raising error when initial position is wrong
            raise RotorConfigurationRingSettingError

        self._notch_position = char_to_int(notch_position)
        self._wiring = [char_to_int(letter) for letter in wiring]
        self._reveresed_wiring = [0] * len(self._wiring)  # Creates list - lenght same as wiring
        for index, value in enumerate(self._wiring):
            self._reveresed_wiring[value] = index

        self._initial_position = char_to_int(initial_poition)
        self._ring_setting = char_to_int(ring_setting)

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
    def ring_setting(self):
        return self._ring_setting

    def step(self):
        pass

    def encript_forward(self):
        pass

    def encript_backward(self):
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
