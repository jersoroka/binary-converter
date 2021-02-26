from typing import List

'''functions used for binary conversion'''


def find_exponent(i: int) -> int:
    """Produce the largest power of two found in i

    ;param i: int, where i > 0
    ;return: int

    Accumulators:
    exp:  value of the exponent to be checked
    diff: n - 2**exp
    """
    exp = 0
    diff = i
    while diff > 0:
        diff = i - (2 ** exp)
        exp += 1
    if diff == 0:
        return exp - 1
    return exp - 2


def make_binary(loi: List[str]) -> str:
    """Produce a binary value with 1's at each position in n

    ;param loi: list, where loi != []
    ;return: str

    Accumulators:
    binary_str: current string of binary values
    """
    binary_str = ""
    for val in range(0, max(loi) + 1):
        if val in loi:
            binary_str += "1"
        else:
            binary_str += "0"
    return binary_str[::-1]


def find_binary(i: int) -> str:
    """produce the binary of i before two's complement

    ;param i: int, where i > 0
    ;return: str

    Accumulators:
    exponents: list of powers of two
    val:       current val
    """
    exponents = []
    val = i
    while val != 0:
        exp = find_exponent(val)
        diff = val - (2 ** exp)
        exponents.append(exp)
        val = diff
    return make_binary(exponents)


def twos_complement(i: str) -> str:
    """Produce the two's complement of i

    ;param i: str, where i != "" and i != "0"
    ;return: str

    Accumulators:
    flipped: two's complemented integers
    """
    flipped = ""
    for digit in i:
        if digit == "1":
            flipped += "0"
        else:
            flipped += "1"

    if flipped[-1] == "0":
        flipped = flipped[0:-1] + "1"
        return flipped
    else:
        indexes = []
        for index in range(len(flipped)):
            if flipped[index] == "0":
                indexes.append(index)
        high = max(indexes)
        flipped = flipped[0:high] + "1" + ((len(flipped)) - (high + 1)) * "0"
        return flipped
