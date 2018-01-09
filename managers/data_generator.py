import os
import errno
from utils.file import write


def create_master_dataset(path, size):
    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

def create_hidden_file(path, size):
    file_name = "{}/.{}".format(path, size)

    write(size, file_name)
