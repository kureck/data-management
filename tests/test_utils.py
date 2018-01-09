from utils.helpers import convert_to_pairs


class TestUtils(object):

    def test_convert_string_list_tuple_pairs(self):
        string_values = "sensors,64,cars,128,mobiles,256"

        expected = [("sensors", "64"), ("cars", "128"), ("mobiles", "256")]

        value = convert_to_pairs(string_values)

        assert expected == value
