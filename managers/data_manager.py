"""
    managers.data_manager
    ~~~~~~~~~~~~~~~~~~~~~
    Simple methods to transform strings and data objects
"""

import os
import shutil
import errno
import random
import string
import collections
import datetime
from utils.file import write, read
from utils.helpers import dataset_control_hash

MB = 1024 * 1024

def create_directory(path, folders=[], size=None):
    """ Create directory.
        The optional params are there as a flag to know if it's a root folder
        or subfolders. Beyond that, it creates a dataset control file.

        :param path: string path where must be writen
               folders: list of subdirectories
               size: file size to be created.
    """

    if os.path.isdir(path):
        shutil.rmtree(path)
    os.makedirs(path)
    create_dataset_control_file(path, folders, size)


def create_dataset_control_file(path, folders, size):
    """ Create a control file for the dataset to be used in update routine.

        :param path: string path where must be writen
               folders: list of subdirectories
               size: file size to be created.
    """
    if size is not None:
        file_name = "{}/dataset_control.json".format(path)
        control = dataset_control_hash(size, folders)
        write(control, file_name)


def create_file_by_size(path, size):
    """ Create file with random strings with given size.
        Is good to notice that this method could be improved by using other
        ways of generating or simulating random chars.
        Following is a reference to try in the future.
        http://jessenoller.com/blog/2008/05/30/making-re-creatable-random-data-files-really-fast-in-python

        :param path: path where must be writen
               size: size of the file that should be created.
                     This is the amount of chars in the file
    """

    m = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(size)])
    write(m, path)


def populate_folder(dir_path, folder_size, file_size):
    """ Create files based on folder and file size.

        :param dir_path: path where file should be writen
               folder_size: maximum folder size.
               file_size: size of the file
    """
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
    """ Method responsible to generate all the structure based on master path, file size
        and folders and its respective size.

        :param master_path: root path where everything will be created
               files_size: size each file must have
               folders_name_size: subfolders and its respective maximum size
    """
    create_directory(master_path, folders_name_size, files_size)
    for folder in folders_name_size:
        for key in folder.keys():
            create_directory(key)
            populate_folder(key, folder.get(key), files_size)


def update_data(master_path, folders_name_size):
    """ Method responsible to update subdirectories size amount and filling with files.

        :param master_path: root path where everything will be updated
               folders_name_size: subfolders and its respective maximum size
    """
    control_file_path = "{}/dataset_control.json".format(master_path)
    control = read(control_file_path)
    files_size = control.get("file_size")
    for folder in folders_name_size:
        for key in folder.keys():
            populate_folder(key, folder.get(key), files_size)
    old_folders = control.get("folders")
    updated = collections.Counter()
    for d in folders_name_size + old_folders:
        updated.update(d)
    control["folders"] = updated
    write(control, control_file_path)

def backup_data(master_path, backup_path):
    """ Method responsible to backup all structure to another folder keeping olders backups.

        :param master_path: root path where everything will be backedup
               backup_path: backup path
    """
    now = datetime.datetime.utcnow()
    timestamp = now.strftime("%Y%m%d%H%M%S%f")
    master_name = os.path.split(master_path)[-1]

    timed_backup_path = "{}/{}_{}".format(backup_path, timestamp, master_name)

    if not os.path.exists(backup_path):
        os.makedirs(backup_path)

    shutil.copytree(master_path, timed_backup_path)
