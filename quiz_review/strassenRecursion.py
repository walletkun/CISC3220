def add_matrices(A,B):
    """
    Add Two matrices element wise
    """
    n = len(A)

    C = [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]
    return C


def subtract_matrices(A,B):
    """
    Subtracting two matrices element wise
    """
    n = len(A)

    C = [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]
    return C


def splitMatrix(A):
    n = len(A)
    mid = n // 2

    A11 = [[A[i][j] for j in range(mid)] for i in range(mid)]
    A12 = [[A[i][j] for j in range(mid, n)] for i in range(mid)]
    A21 = [[A[i][j] for j in range(mid)] for i in range(mid, n)]
    A22 = [[A[i][j] for j in range(mid, n)] for i in range(mid, n)]
    
    return A11,A12,A21,A22


def mergeMatrix(C11,C12,C21,C22):
    n = len(C11) * 2

    C = [[0] * n for _ in range(n)]


    mid = n // 2

    for i in range(mid):
        for j in range(mid):
            C[i][j] = C11[i][j]
            C[i][j + mid] = C12[i][j]
            C[i + mid][j] = C21[i][j]
            C[i + mid][j + mid] = C22[i][j]

    return C



def strassen_recursive(A,B):
    n = len(A)

    if n == 1:
        return [[A[0][0] * B[0][0]]]



    # First divide matrices into 4 submatrices
    A11, A12, A21, A22 = splitMatrix(A)
    B11, B12, B21, B22 = splitMatrix(B)


    # Second compute the 7 matrices with matrix multiplcation recursively
    M1 = strassen_recursive(add_matrices(A11, A22), add_matrices(B11, B22))
    M2 = strassen_recursive(add_matrices(A21, A22), B11)
    M3 = strassen_recursive(A11, subtract_matrices(B12, B22))
    M4 = strassen_recursive(A22, subtract_matrices(B21, B11))
    M5 = strassen_recursive(add_matrices(A11, A12), B22)
    M6 = strassen_recursive(subtract_matrices(A21, A11), add_matrices(B11, B12))
    M7 = strassen_recursive(subtract_matrices(A12, A22), add_matrices(B21, B22))



    C11 = add_matrices(subtract_matrices(add_matrices(M1, M4), M5), M7)
    C12 = add_matrices(M3, M5)
    C21 = add_matrices(M2, M4)
    C22 = add_matrices(add_matrices(subtract_matrices(M1, M2), M3), M6)

    return mergeMatrix(C11,C12,C21,C22)


A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
B = [[17, 18, 19, 20], [21, 22, 23, 24], [25, 26, 27, 28], [29, 30, 31, 32]]

C = strassen_recursive(A, B)

print(C)
