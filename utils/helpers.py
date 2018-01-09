def convert_to_pairs(args):
    data = args.split(",")

    return [(x, y) for x, y in zip(data[0::2], data[1::2])]
