import json

def write(content, file_name):
    with open(file_name, 'w') as writer:
        if file_name.endswith('.json'):
            json.dump(content, writer)
        else:
            writer.write(content)


def read():
    pass
