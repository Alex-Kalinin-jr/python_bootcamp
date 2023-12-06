import sys
import os
sys.path.append(os.path.abspath('../ex00'))
sys.path.append(os.path.abspath('../ex01'))
from file import add_ingot, empty, get_ingot
from split_booty import split_booty


def squeak_decorator(func):
    def wrapper(*args):
        print('SQUEAK')
        return func(*args)
    return wrapper


empty = squeak_decorator(empty)
add_ingot = squeak_decorator(add_ingot)
get_ingot = squeak_decorator(get_ingot)
split_booty = squeak_decorator(split_booty)

def main():
    a = {"ab":3, "cd":4, "gold_ingots":11}
    b = add_ingot(a)
    c = empty(a)
    d = split_booty(c, a, b, b)
    e = split_booty(c, a, b, b, b)
    f = split_booty(c, a)
    print(d)
    print(e)
    print(f)

if __name__ == "__main__":
    main()
