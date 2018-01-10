import json

def write(content, file_name):
    with open(file_name, 'w') as writer:
        if file_name.endswith('.json'):
            json.dump(content, writer)
        else:
            writer.write(content)


def read(file_name):
    with open(file_name) as data:
        loaded_file = json.load(data)

    return loaded_file
