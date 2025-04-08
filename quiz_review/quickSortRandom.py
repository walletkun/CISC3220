import random as rd
def quickSortRandom(arr, low, high):
    if low >= high:
        return
    pivot_index = rd.randint(low, high)
    arr[pivot_index],arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high] # since we swapped it with the pivot index therefore it is the last element

    left = low
    right = high

    while left < right:
        while arr[left] <= pivot and left < right:
            left += 1

        while arr[right] >= pivot and left < right:
            right -= 1


        if left < right:
            arr[left], arr[right] = arr[right],arr[left]


    arr[left],arr[high] = arr[high],arr[left]


    quickSortRandom(arr, low, left - 1)
    quickSortRandom(arr, left + 1, high)



arr = [10, 80, 30, 90, 40, 50, 70]
quickSortRandom(arr, 0, len(arr) - 1)
print(arr)