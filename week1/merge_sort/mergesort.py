def mergeSort(A : list[int], p: int, r: int):
    if p >= r:
        return

    q = (p + r) // 2

    mergeSort(A, p , q)
    mergeSort(A, q + 1 , r)

    merge(A, p, q, r)


def merge(A: list[int], p : int, q: int, r: int):
    n1 = q - p + 1
    n2 = r - q

    left = [0] * n1
    right = [0] * n2

    for i in range(len(left)):
        left[i] = A[p + i]


    for i in range(len(right)):
        right[i] = A[q + 1 + i]

    i, j , k = 0, 0, p

    while i < n1 and j < n2:
        if (left[i] <= right[j]):
            A[k] = left[i]
            i += 1

        else:
            A[k] = right[j]
            j += 1

        k += 1


    while i < n1:
        A[k] = left[i]
        i += 1
        k += 1

    while j < n2:
        A[k] = right[j]
        j += 1
        k += 1


nums = [1,5,4,2]
mergeSort(nums, 0, len(nums) - 1)
print(nums)

    
    