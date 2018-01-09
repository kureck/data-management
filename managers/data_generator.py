import os
import errno
import random
import string
from utils.file import write

MB = 1024 * 1024

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

def populate_folder(dir_path, folder_size, file_size):
    left = (folder_size % file_size) * MB
    number_files = folder_size // file_size

    for x in range(number_files):
        file_name = "file{}".format(x)
        file_path = "{}/{}".format(dir_path, file_name)
        create_file_by_size(file_path, file_size * MB)

    if left:
        file_name = "file{}".format(number_files+1)
        file_path = "{}/{}".format(dir_path, file_name)
        create_file_by_size(file_path, left * MB)
