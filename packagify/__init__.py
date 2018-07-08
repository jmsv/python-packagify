import argparse

parser = argparse.ArgumentParser()
parser.add_argument('entry', type=argparse.FileType('r'))
args = parser.parse_args()

print(args.entry.name)
entry_point_lines = [line.strip() for line in args.entry.readlines()]
print(entry_point_lines)
