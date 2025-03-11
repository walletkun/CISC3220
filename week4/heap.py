# Max heap
def heapify(arr, n, i):
    # Initialize the largest as the root
    largest = i
    # Left child and right child are defined as 2 * the current index (i) + 1 is the left child
    left = 2 * i + 1
    # Right child is represented with 2 * i + 2
    right = 2 * i + 2


    # Checking to see if the left child of the root exist and is greater than the root
    if left < n and arr[i] < arr[left]:
        largest = left


    # Vice versa for the right child
    if right < n and arr[largest] < arr[right]:
        largest = right


    # Change the root if needed, meaning yes the above condition fails as a heap must have a root that is greater than it's children
    if largest != i:
        # swap
        (arr[i] , arr[largest]) = (arr[largest], arr[i])


        # we call heapify to make sure the heap holds the condition
        heapify(arr, n, largest)


# Heap sort
# The main function to sort an array of given size

def heapSort(arr):
    n = len(arr)


    # Building a maxheap
    # Since the last parent node will be at n // 2 we can start at that location
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)


    # Only by one extract element
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])

        heapify(arr, i, 0)


arr = [12, 56, 13, 12, 10, -1]
print(f"Before sorting is: {[arr[i] for i in range(len(arr))]}")
heapSort(arr)
n = len(arr)
print(f'Sorted array is: {[arr[i] for i in range(n)]}')

    

    