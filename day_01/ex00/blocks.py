# day 01 - aquaintance with arg parsing
import argparse

def main():
    parser = argparse.ArgumentParser(description='blocks')
    parser.add_argument("number", type=int, help='count of iterations')

    out_list = []
    check = lambda x: out_list.append(x) \
        if x.startswith('00000') and len(x) == 32 and x[5] != '0' else None

    for i in range(parser.parse_args().number):
        try:
            check(input())
        except Exception:
            pass
    for i in out_list:
        print(i)

if __name__ == "__main__":
    main()
