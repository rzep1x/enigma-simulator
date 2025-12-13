from utils import char_to_int, int_to_char


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
    def __init__(self, notch_position: chr, wiring : str, initial_poition: chr):
        self._notch_position = char_to_int(notch_position)
        self._wiring = [char_to_int(letter) for letter in wiring]
        self._reveresed_wiring = [0] * len(self._wiring)  # Creates list - lenght same as wiring
        for index, value in enumerate(self._wiring):
            self._reveresed_wiring[value] = index
        self._initial_position = char_to_int(initial_poition)
    
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
    
    def step(self):
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