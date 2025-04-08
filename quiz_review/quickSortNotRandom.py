def quickSort(arr:list[int], low:int, high:int) -> list[int]:
    if low >= high:
        return arr


    l = low
    pivot = arr[high]
    r = high

    while l < r:

        while arr[l] <= pivot and l < r:
            l += 1

        while arr[r] >= pivot and l < r:
            r -= 1

        if l < r:
            arr[l],arr[r] = arr[r],arr[l]


    arr[l], arr[high] = arr[high], arr[l]


    quickSort(arr, low, l - 1)
    quickSort(arr, l + 1, high)


arr = [10, 80, 30, 90, 40, 50, 70]
quickSort(arr, 0, len(arr) - 1)
print(arr)


    