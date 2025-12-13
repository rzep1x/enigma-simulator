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

        # Validation for notch position
        if not isinstance(notch_position, str) or len(notch_position) != 1:
            raise RotorConfigurationNotchPositionError
        if not notch_position.isascii() or not notch_position.isalpha():
            # raising error when notch_position_is_not_from_latin_alphabet
            # .isalpha() checks for special characters
            # .isascii() checks for non ascii characters like ą,ł,ć etc
            #  checks for letters than
            raise RotorConfigurationNotchPositionError

        # Validation for wiring
        if not isinstance(wiring, str) or len(wiring) != 26:
            raise RotorConfigarationWiringError
        if not wiring.isalpha() or not notch_position.isascii():
            raise RotorConfigarationWiringError

        # Validation for initial postion
        if not isinstance(initial_poition, str) or len(initial_poition) != 1:
            raise RotorConfigurationInitialPositionError
        if not initial_poition.isalpha() or not initial_poition.isascii():
            raise RotorConfigurationInitialPositionError

        # Validation for ring_setting
        if not isinstance(ring_setting, str) or len(ring_setting) != 1:
            raise RotorConfigurationRingSettingError
        if not ring_setting.isalpha() or not ring_setting.isascii():
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
