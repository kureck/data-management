def convert_to_pairs(master_path, args):
    data = args.split(",")

    return [{"{}/{}".format(master_path, x): int(y)} for x, y in zip(data[0::2], data[1::2])]


def dataset_control_hash(file_size, files):
    return {"file_size": file_size, "folders": files}
