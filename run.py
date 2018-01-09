import argparse

parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers(help="sub-command help")
g1 = subparsers.add_parser('data-generation', help='Generate Dataset')
g1.set_defaults(which="data-generation")
g1.add_argument("--master-dataset-path", '-m', help='Set the master dataset path', required=True)
g1.add_argument("--files-size", '-fs', help='Set files size', required=True)
g1.add_argument("--files-name-size", '-fns', help='Set files name and size: <name1>,<size1><name2>,<size2>', required=True)
g2 = subparsers.add_parser("data-update", help="Updates a given Master Dataset")
g2.set_defaults(which="data-update")
g2.add_argument("--master-dataset-path", "-mp", help='Master dataset path', required=True)
g2.add_argument("--files-name-size", '-fns', help='Set files name and size to update: <name1>,<size1><name2>,<size2>', required=True)
g3 = subparsers.add_parser("data-backup", help="Backup a given Master Dataset")
g3.set_defaults(which="data-backup")
g3.add_argument("--master-dataset-path", "-mp", help='Master dataset path', required=True)
g3.add_argument("--backup-destination", '-bp', help='Backup path', required=True)

args = parser.parse_args()


def run():
    if args.which == "data-generation":
        print("data-generation")
    elif args.which == "data-update":
        print("data-update")
    elif args.which == "data-backup":
        print("data-backup")


if __name__ == "__main__":
    run()
