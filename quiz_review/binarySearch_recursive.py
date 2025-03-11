def binary_recursive(arr: list[int], low:int, high:int, target: int) -> int:

    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            return binary_recursive(arr, mid + 1, high, target)

        else:
            return binary_recursive(arr, low, mid - 1, target)
    else:
        return -1


arr = [ 2, 3, 4, 10, 40 ]
x = 10

print(binary_recursive(arr, 0, len(arr)-1, x))
