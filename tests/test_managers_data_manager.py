import os
import shutil
from managers.data_manager import create_directory
from managers.data_manager import create_file_by_size
from managers.data_manager import populate_folder


class TestManagersDataGeneration(object):

    def setup(self):
        self.master_data_path = 'tests/data/master-dataset'

    def test_create_master_dataset(self):
        if os.path.isdir(self.master_data_path):
            shutil.rmtree(self.master_data_path)

        folder = [{"sensors": 64}]
        size = 2

        create_directory(self.master_data_path, folder, size)

        expected = True
        value = os.path.isdir(self.master_data_path)

        assert expected == value

    def test_create_master_dataset_with_control_file(self):
        folder = [{"sensors": 64}]
        file_size = 2

        if os.path.isdir(self.master_data_path):
            shutil.rmtree(self.master_data_path)

        create_directory(self.master_data_path, folder, file_size)

        expected = True
        file_value = os.path.exists("{}/dataset_control.json".format(self.master_data_path))

        assert expected == file_value

    def test_create_dataset_directories(self):
        path = "sensors"

        file_path = "{}/{}".format(self.master_data_path, path)

        if os.path.isdir(file_path):
            shutil.rmtree(file_path)

        create_directory(file_path)

        expected = True
        value = os.path.isdir(file_path)

        assert expected == value

    def test_create_file_by_size(self):
        size = 2
        file_size = 2*1024*1024  # 2097125

        path = "sensors"

        dir_path = "{}/{}".format(self.master_data_path, path)

        if os.path.isdir(dir_path):
            shutil.rmtree(dir_path)

        create_directory(dir_path)

        file_name = "file1"
        file_path = "{}/{}/{}".format(self.master_data_path, path, file_name)

        create_file_by_size(file_path, file_size)

        value = os.path.getsize(file_path)

        assert value == file_size

    def test_create_two_files_same_size_given_dir_size(self):
        MB = 1024*1024
        file_size = 2
        folder_size = 4

        path = "sensors"

        dir_path = "{}/{}".format(self.master_data_path, path)

        if os.path.isdir(dir_path):
            shutil.rmtree(dir_path)

        create_directory(dir_path)

        populate_folder(dir_path, folder_size, file_size)

        value = sum(os.path.getsize("{}/{}".format(dir_path, f)) for f in os.listdir(dir_path) if os.path.isfile("{}/{}".format(dir_path,f)))

        expected = folder_size * MB

        assert value == expected

    def test_create_two_files_diff_sizes_given_dir_size(self):
        MB = 1024*1024
        file_size = 2
        folder_size = 5

        path = "sensors"

        dir_path = "{}/{}".format(self.master_data_path, path)

        if os.path.isdir(dir_path):
            shutil.rmtree(dir_path)

        create_directory(dir_path)

        populate_folder(dir_path, folder_size, file_size)

        value = sum(os.path.getsize("{}/{}".format(dir_path, f)) for f in os.listdir(dir_path) if os.path.isfile("{}/{}".format(dir_path,f)))

        expected = folder_size * MB

        assert value == expected
