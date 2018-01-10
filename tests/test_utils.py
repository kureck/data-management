from utils.helpers import convert_to_pairs
from utils.helpers import dataset_control_hash


class TestUtils(object):

    def test_convert_string_list_tuple_pairs_with_master_path(self):
        string_values = "sensors,64,cars,128,mobiles,256"
        master_path = "master_path"

        expected = [("master_path/sensors", 64), ("master_path/cars", 128), ("master_path/mobiles", 256)]

        value = convert_to_pairs(master_path, string_values)

        assert expected == value

    def test_create_dataset_control_hash(self):
        files = [("sensors", 64), ("cars", 128), ("mobiles", 256)]
        file_size = 2

        expected = {"file_size": file_size,
                    "folders": files}

        value = dataset_control_hash(file_size, files)

        assert value == expected
