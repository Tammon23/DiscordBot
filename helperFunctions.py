import os

def folderMaker(path):
    """
    Checks if a config folder exists.
    If not it will create one.
    Whether one is create or not will decide
    the boolean return

    """

    if os.path.exists(path):
        return False

    else:
        os.mkdir(path)
        return True

def saveListToFile(data: list, filename: str, overwrite=True):
    """
    Saves a list into a given file
    :param data: 
    :param filename: 
    :param overwrite: 
    :return: bool 
    """""
    if os.path.exists(filename):
        if not overwrite:
            return False

    with open(filename, 'w') as f:
        for title in data:
            f.write(str(title) + "\n")
    return True


def readListFromFile(filename: str):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return [line.rstrip('\n') for line in f]

    else:
        return []