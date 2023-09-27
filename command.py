import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-s", "--size", help = "The size")

args = arg_parser.parse_args()
size = args.size

print(size)