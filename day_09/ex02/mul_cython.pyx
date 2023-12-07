from libc.stdlib cimport malloc, free

def check_matrix_type_int(a):
    cdef int i, j
    for i in range(len(a)):
        for j in range(len(a[i])):
            if not isinstance(a[i][j], int):
                raise TypeError("matrix must be a list of integers")
    return True

def check_sizes(a, b):
    cdef int i
    for i in range(len(a)):
        if len(a[i]) != len(b):
            raise TypeError("lists must have the same size")
    
    if len(a) > 100 or len(b) > 100 or any(len(inner) > 100 for inner in a + b):
        raise TypeError("matrix size must be less than 100")
    
    return True

def mul(a, b):
    check_matrix_type_int(a)
    check_matrix_type_int(b)
    check_sizes(a, b)
    
    cdef int i, j, k
    cdef int rows_a = len(a)
    cdef int cols_a = len(a[0])
    cdef int cols_b = len(b[0])
    cdef int** result = allocate_2d_array(rows_a, cols_b)
    
    for i in range(rows_a):
        for j in range(cols_b):
            result[i][j] = 0
            for k in range(cols_a):
                result[i][j] += a[i][k] * b[k][j]
    
    cdef list result_list = [[result[i][j] for j in range(cols_b)] for i in range(rows_a)]
    
    free_2d_array(<int**>result, rows_a)
    
    return result_list

cdef int** allocate_2d_array(int rows, int cols):
    cdef int** arr = <int**>malloc(rows * sizeof(int*))
    for i in range(rows):
        arr[i] = <int*>malloc(cols * sizeof(int))
    return arr

cdef void free_2d_array(int** arr, int rows):
    for i in range(rows):
        free(arr[i])
    free(arr)