import os
import shutil
from managers.data_generator import create_directory
from managers.data_generator import create_hidden_file


class TestManagersDataGeneration(object):

    def setup(self):
        self.master_data_path = 'tests/data/master-dataset'
        self.size = "64"

    def test_create_master_dataset(self):
        if os.path.isdir(self.master_data_path):
            shutil.rmtree(self.master_data_path)

        create_directory(self.master_data_path, self.size)

        expected = True
        value = os.path.isdir(self.master_data_path)

        assert expected == value

    def test_create_hidden_size_file(self):
        create_hidden_file(self.master_data_path, self.size)

        expected = True
        value = os.path.exists("{}/.{}".format(self.master_data_path, self.size))

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
