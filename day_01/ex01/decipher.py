import argparse

parser = argparse.ArgumentParser(description='decipher')
parser.add_argument("string", type=str, help='expression for parsing')
print (''.join([x[0] for x in parser.parse_args().string.split()]))


# python decypher.py "Have you delivered eggplant pizza at restored keep?"