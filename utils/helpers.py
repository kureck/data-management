"""
    utils.helpers
    ~~~~~~~~~~~~~
    Simple methods to transform strings and data objects
"""


def convert_to_pairs(master_path, args):
    """ Converts string into a key value pair format.

        :param master_path: path where files should be writen
               args: a string in format "<name>,<number>,<name>,<number>"
                     ex.: "sensors,1,cars,2,web,3"
        :returns: a list of dicts
                  ex.: [{"sensors": 1}, {"cars": 2}, {"web": 3}]
    """
    data = args.split(",")

    return [{"{}/{}".format(master_path, x): int(y)} for x, y in zip(data[0::2], data[1::2])]


def dataset_control_hash(file_size, folders):
    """ Creat structure to be writen in a json file.

        :param file_size: size of each file tha will be created
               folders: list of dicts
        :returns: a dict
    """
    return {"file_size": file_size, "folders": folders}
