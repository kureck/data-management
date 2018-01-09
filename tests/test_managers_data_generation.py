import os
import shutil
from managers.data_generator import create_directory
from managers.data_generator import create_file_by_size
from managers.data_generator import populate_folder


class TestManagersDataGeneration(object):

    def setup(self):
        self.master_data_path = 'tests/data/master-dataset'

    def test_create_master_dataset(self):
        if os.path.isdir(self.master_data_path):
            shutil.rmtree(self.master_data_path)

        create_directory(self.master_data_path)

        expected = True
        value = os.path.isdir(self.master_data_path)

        assert expected == value

    def test_create_dataset_directories(self):
        args = ("sensors", "64")
        path, size = args

        file_path = "{}/{}".format(self.master_data_path, path)

        if os.path.isdir(file_path):
            shutil.rmtree(file_path)

        create_directory(file_path, size)

        expected = True
        value = os.path.isdir(file_path)

        assert expected == value

    def test_create_directories_with_hidden_file(self):
        args = ("sensors", "64")
        path, size = args

        file_path = "{}/{}".format(self.master_data_path, path)

        if os.path.isdir(file_path):
            shutil.rmtree(file_path)

        create_directory(file_path, size)

        expected = True
        path_value = os.path.isdir(file_path)
        file_value = os.path.exists("{}/.{}".format(file_path, size))

        assert expected == path_value
        assert expected == file_value

    def test_create_file_by_size(self):
        size = 2
        file_size = 2*1024*1024  # 2097125

        args = ("sensors", "64")
        path, size = args

        dir_path = "{}/{}".format(self.master_data_path, path)

        if os.path.isdir(dir_path):
            shutil.rmtree(dir_path)

        create_directory(dir_path, size)

        file_name = "file1"
        file_path = "{}/{}/{}".format(self.master_data_path, path, file_name)

        create_file_by_size(file_path, file_size)

        value = os.path.getsize(file_path)

        assert value == file_size

    def test_create_two_files_given_dir_size(self):
        MB = 1024*1024
        file_size = 2 * MB
        folder_size = 4 * MB

        args = ("sensors", "64")
        path, size = args

        dir_path = "{}/{}".format(self.master_data_path, path)

        if os.path.isdir(dir_path):
            shutil.rmtree(dir_path)

        create_directory(dir_path, size)

        file_name = "file1"
        file_path = "{}/{}/{}".format(self.master_data_path, path, file_name)

        populate_folder(dir_path, folder_size, file_size)

        value = sum(os.path.getsize("{}/{}".format(dir_path, f)) for f in os.listdir(dir_path) if os.path.isfile("{}/{}".format(dir_path,f)))

        assert value == folder_size
