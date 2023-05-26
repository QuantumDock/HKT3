from math import log2
CALC_FACTOR = 348441290  # source unreliable: quora
def entropy_calculator(string: str) -> float:
    flags = [False, False, False, False]
    numbered_string = [ord(i) for i in string]
    dictionary_factor = 1
    for char in numbered_string:
        if char in range(48, 58):  # [0-9]
            flags[0] = True
        elif char in range(65, 91):  # [A-Z]
            flags[1] = True
        elif char in range(97, 123):  # [a-z]
            flags[2] = True
        elif char in range(32, 48) or char in range(58, 65) or char in range(91, 97) or char in range(123, 127):
            flags[3] = True
        else:  # chars outside ascii, add check for that in flask
            raise ArithmeticError
    file = [i[:-1] for i in open("static/dictionary.txt", "rt").readlines()] # reads text except \n
    for j in file:
        if j in string:
            dictionary_factor *= 6 if dictionary_factor == 1 else 3
    return ((log2(10*flags[0] + 26*flags[1] + 26*flags[2] + 32*flags[3]))*len(string))/dictionary_factor


def time_to_crack(string: str) -> float:
    return 2**(entropy_calculator(string))/CALC_FACTOR


