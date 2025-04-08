def count_sort(A, n , k):
    B = [0] * n
    C = [0] * k

    for i in range(n):
        C[A[i]] += 1

    for i in range(1, k):
        C[i] += C[i - 1]

    print("Prefix Sum:", C)

    for i in range(n - 1, -1 ,-1):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1

    print(B)

count_sort([3,2,2,1,1], 5, k= max([3,2,2,1,1]) + 1)

    
    
    