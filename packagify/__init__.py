import argparse
import os
import re


def get_imports(lines):
    regex_packages = [
        re.compile(r'^\s*import\s+(?P<p>[\w\d_]+)'),
        re.compile(r'^\s*from\s+(?P<p>[\w\d_]+)')
    ]

    imports = []
    for line in lines:
        for search in regex_packages:
            imports.extend(re.findall(search, line))

    return imports


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('entry', type=argparse.FileType('r'))
    args = parser.parse_args()

    entry_path = os.path.abspath(args.entry.name)
    print('Entry file:\t', entry_path)

    entry_dir = os.path.dirname(entry_path)
    print('Entry dir:\t', entry_dir)

    entry_point_lines = [line.strip() for line in args.entry.readlines()]

    print('Imports:\t', get_imports(entry_point_lines))


if __name__ == '__main__':
    main()
