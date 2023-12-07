from itertools import tee 


def check_matrix_type_int(a: list[list[int]]) -> bool:
    if any(not isinstance(val, int) for row in a for val in row):
        raise TypeError("matrix must be a list of integers")
    return True

from typing import List

def check_sizes(a: List[List[int]], b: List[List[int]]) -> bool:
    if any(len(inner_list) != len(b) for inner_list in a):
        raise TypeError("lists must have the same size")
    
    if any(len(inner) > 100 for inner in a + b) or len(a) > 100 or len(b) > 100:
        raise TypeError("matrix size must be less than 100")
    
    return True

def mul(a, b):
    check_matrix_type_int(a)
    check_matrix_type_int(b)
    check_sizes(a, b)
    b_iter = tee(zip(*b), len(a))
    return [
        [
            sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b)) 
            for col_b in b_iter[i]
        ] for i, row_a in enumerate(a)
    ]


def main():
    x = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    y = [[1,2],[1,2],[3,4]]
    print(mul(x, y))

if __name__ == "__main__":
    main()