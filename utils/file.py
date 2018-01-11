"""
    utils.file
    ~~~~~~~~~~
    Reads and writes json and dummy files.
    json: loads and writes generic json files.
    dummy files: files with random characters inside of it
"""

import json

def write(content, file_name):
    """ Write both csv and json files.

        :param file_name: string with name of the file
               content: string or dict to be saved on file
    """
    with open(file_name, 'w') as writer:
        if file_name.endswith('.json'):
            json.dump(content, writer)
        else:
            writer.write(content)


def read(file_name):
    """ Read json files.

        :param file_name: path where must be writen
        :returns: a dict
    """
    with open(file_name) as data:
        loaded_file = json.load(data)

    return loaded_file
