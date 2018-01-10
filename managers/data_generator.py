import os
import shutil
import errno
import random
import string
from utils.file import write
from utils.helpers import dataset_control_hash

MB = 1024 * 1024

def create_directory(path, folders=[], size=None):
    if os.path.isdir(path):
        shutil.rmtree(path)
    os.makedirs(path)
    create_dataset_control_file(path, folders, size)


def create_dataset_control_file(path, folders, size):
    if size is not None:
        file_name = "{}/dataset_control.json".format(path)
        control = dataset_control_hash(size, folders)
        write(control, file_name)


def create_file_by_size(path, size):
    # http://jessenoller.com/blog/2008/05/30/making-re-creatable-random-data-files-really-fast-in-python
    m = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(size)])
    write(m, path)


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
        create_file_by_size(file_path, left)


def generate_data(master_path, files_size, folders_name_size):
    create_directory(master_path, folders_name_size, files_size)
    for folder in folders_name_size:
        create_directory(folder[0])
        populate_folder(folder[0], folder[1], files_size)
