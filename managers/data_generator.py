import os
import errno
import random
import string
from utils.file import write


def create_directory(path, size=None):
    try:
        os.makedirs(path)
        create_hidden_file(path, size)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def create_hidden_file(path, size):
    if size is not None:
        file_name = "{}/.{}".format(path, size)

        write(size, file_name)

def create_file_by_size(path, size):
    # http://jessenoller.com/blog/2008/05/30/making-re-creatable-random-data-files-really-fast-in-python
    m = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(size)])
    with open(path, 'w') as writer:
        writer.write(m)
