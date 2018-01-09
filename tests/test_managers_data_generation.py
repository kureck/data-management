import os
import shutil
from managers.data_generator import create_master_dataset
from managers.data_generator import create_hidden_file


class TestManagersDataGeneration(object):

    def setup(self):
        self.master_data_path = 'tests/data/master-dataset'
        self.size = "64"

    def test_create_master_dataset(self):
        if os.path.isdir(self.master_data_path):
            shutil.rmtree(self.master_data_path)

        create_master_dataset(self.master_data_path, self.size)

        expected = True
        value = os.path.isdir(self.master_data_path)

        assert expected == value

    def test_create_hidden_size_file(self):
        create_hidden_file(self.master_data_path, self.size)

        expected = True
        value = os.path.exists("{}/.{}".format(self.master_data_path, self.size))

        assert expected == value