from string import ascii_lowercase, digits
import numpy as np
from collections import deque
from assitance import getStandardCharset, loadCharset


def processCharactor(char, table: deque, memory: np.ndarray, charset):

    """
    Called by train function in every iteration to update "table" (numpy array) and "memory" (deque) with char.

    Increment value in specific index by 1,
    the index is determine from "memory", each combination corespondent to unique index.
    This have effect of counting a number of times


    :param char:
    :param table:
    :param memory:
    :param charset:
    :return:
    """

    charnum = charset[char]

    try:
        table[tuple(memory)][charnum] += 1
    except IndexError as error:
        print(error)
        print(memory[0])
        exit()

    memory.append(charnum)


def train(filepath, charset, blocksize=1):

    CHARLENGTH = int(len(charset)/2)
    table = np.ones([CHARLENGTH] * (blocksize + 1), dtype=np.float32) * (3e-4 ** blocksize)
    # small inital to prevent 0 division error)

    memory = deque(maxlen=blocksize)

    with open(filepath, "r") as file:

        firstLine = next(file)
        for i, j in enumerate(firstLine):
            if i < blocksize:
                memory.append(charset[j])
            else:
                processCharactor(j, table, memory, charset)

        for line in file:
            for char in line:
                processCharactor(char, table, memory, charset)

    return table / np.sum(table, axis=-1, keepdims=True)


if __name__ == '__main__':

    np.set_printoptions(suppress=True)

    # uncomment for standard charset
    # charset = getStandardCharset()

    charset = loadCharset("../charset/lyrics.txt")

    table = train("../data/Demons.txt", charset=charset, blocksize=5)

    # print(table)
    # print(table.shape)
    # print(np.argmax(table, axis=-1))

    np.save("../model/demons5.npy", table)
