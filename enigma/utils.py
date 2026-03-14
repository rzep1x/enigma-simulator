def char_to_int(char):
    return ord(char.upper()) - 65


def int_to_char(number):
    return chr((number % 26) + 65)
