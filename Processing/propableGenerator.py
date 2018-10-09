import numpy as np
from assitance import getStandardCharset, loadCharset
from sys import argv


def generateNumCharString(table, startingChar, size, charset):

    """
    generate number sequence using propabilty derived from table

    :param table: propability table used for generating each next charactor
    :param startingChar: first charactors in string (interally converted to number), must be corresponed with table's
    observation char length
    :param size: length of charactor in genereated number sequence
    :param charset: charset used in coverting between number and char, returned from assitance.loadCharset method
    :return: number sequence generated using propability from table, starting with startingChar
    """

    charCount = len(table.shape) - 1
    text = [charset[i] for i in startingChar]

    assert len(text) == charCount

    for i in range(size):

        # OPTIMIZABLE: use deque to keep track for N-last char
        indiecs = tuple([text[-charCount + i] for i in range(charCount)])

        prop = table[indiecs]

        nextNum = np.random.choice(range(prop.shape[-1]), p=prop)
        text.append(nextNum)

    return text


def numCharStringToString(numCharString, charset: dict):

    """
    Convert Sequence of number to string using charset

    :param numCharString: Squence of number to be converted
    :param charset: charset used in conversion of number to charactor, usually returned from assitance.loadCharset
    :return: string converted from numCharString
    """

    return  "".join(map(charset.__getitem__, numCharString))


if __name__ == '__main__':

    # charset = getStandardCharset()
    charset = loadCharset("../charset/lyrics.txt")

    for i in (4,):
        table = np.load("../model/demons{}.npy".format(i))
        print("\nComplexity", i)
        numCharString = generateNumCharString(table, 'look'[:i], 1000, charset)
        string = numCharStringToString(numCharString, charset)
        print(string)
