import sys
import os
sys.path.append(os.path.abspath('../ex00'))
from file import add_ingot, empty

def split_booty(*args):
    sum_count = sum(arg.get('gold_ingots', 0) for arg in args)
    reminder = sum_count % 3

    buff_list = []
    for i in range(3):
        if i < len(args):
            dict_copy = dict(args[i])
        else:
            dict_copy = {'gold_ingots': 0}

        if reminder == 2 and i != 2 or reminder == 1 and i == 2:
            dict_copy['gold_ingots'] = sum_count // 3 + 1
        else:
            dict_copy['gold_ingots'] = sum_count // 3

        buff_list.append(dict_copy)

    return tuple(buff_list)


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
