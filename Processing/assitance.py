STANDARDPATH = "../charset/standard.txt"


def loadCharset(filepath):

    """
    load charset text file,
    charset here is dictionary that map char to number and number to char

    the length of charset will greatly influence model file size

    :param filepath: charset file path
    :return: a charset (dictionary) parse from text file in filepath
    """

    charset = dict()

    with open(filepath, 'r') as file:

        i = 0

        for line in file:
            for char in line:
                charset[i] = char
                charset[char] = i
                i += 1

    return charset


def getStandardCharset():

    """
    load standard charset (charset located in path defined by STANDARDPATH constance)

    :return:
    """

    return loadCharset(STANDARDPATH)


if __name__ == '__main__':

    stdCharset = getStandardCharset()

    for i in range(52):
        char = stdCharset[i]
        # print(char, end="")
        print(i, char, stdCharset[char])
