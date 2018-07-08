# Test calling module that can't be found locally
import ety
# Test calling other files in different ways
import imported1  # noqa: F401
from imported2 import what


def uhh():
    return 'uhh'


def tree(word):
    return ety.tree(word)


def use_another_file():
    return what.upper()


if __name__ == '__main__':
    print(uhh())
    print(tree('potato'))
    print(use_another_file())
