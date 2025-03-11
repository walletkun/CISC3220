def matrixMultiplication_recursive(A: list[int], B:list[int], C:list[int], i:int, j:int, k:int, N:int):
    """
    Recursively compute matrix multiplication element C[i][j]
    Args:
        A (list[int]): First Matrix
        B (list[int]): Second Matrix
        C (list[int]): Result Matrix
        i (int): Row index for result matrix
        j (int): Column index for result matrix
        k (int): Iteration index for the summation (recursive loop)
        N (int): Number of columns in A and rows in B
    """

    if k == N:
        return C[i][j] # Finished computing 

    C[i][j] += A[i][k] * B[k][j]


    return matrixMultiplication_recursive(A,B,C, i, j, k + 1, N)


def multiply(A,B):
    """Wrapper function to multiply matrices A and B recursively

    Args:
        A (list[int]): Matrix A
        B (list[int]): Matrix B
    """
    M,N = len(A), len(A[0]) # A is M X N
    P = len(B[0]) # B is N X P

    C = [[0] * P for _ in range(M)] # Initializing the matrix with 0's
    
    def compute(i, j):
        """Compute C[i][j] using recursion

        Args:
            i (int): row index
            j (int): column index
        """

        if i == M: # done with all rows
            return

        if j == P:
            compute(i + 1, 0) # Finished all columns then we continue with new row until the row is finished computing
            return

        # Compute C[i][j]
        C[i][j] = matrixMultiplication_recursive(A,B,C,i,j,0,N)

        compute(i, j + 1)

    # Start recursion
    compute(0, 0)

    return C


A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(multiply(A,B))