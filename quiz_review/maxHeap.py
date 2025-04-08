class MaxHeap:
    def __init__(self, array = None):
        self.heap = array[:] if array else [] # If array exist we copy that array otherwise it's an empty list
        if self.heap:
            self.build_heap() # Covert the array into a valid heap


    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def parent(self, i):
        return (i - 1) // 2


    def heapify(self, i, heap_size = None):
        if heap_size == None:
            heap_size = len(self.heap)
        largest = i
        left = self.left_child(i)
        right = self.right_child(i)


        # Checking if the left child exists and is greater than our current largest
        if left < heap_size and self.heap[left] > self.heap[largest]:
            # Then we swap
            largest = left

        # Same with the right child
        if right < heap_size and self.heap[right] > self.heap[largest]:
            largest = right

        # Then we check if the largest is not the root, then continue heapifying
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify(largest, heap_size) # Recursively do the operation until it's fully heaped



    def build_heap(self):
        n = len(self.heap)
        for i in range(n // 2 - 1, -1 ,-1): # Start heapfying from bottom up
            self.heapify(i)


    def insert(self, value):
        self.heap.append(value)
        index = len(self.heap) - 1

        while index > 0 and self.heap[self.parent(index)] < self.heap[index]:
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index) # Move up



    def extract_max(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()


        max_value = self.heap.pop()
        self.heapify(0)

        return max_value

    def display(self):
        return (self.heap)


    def heapSort(self):
        n = len(self.heap)
        self.build_heap()
        for i in range(n - 1, 0, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            self.heapify(0, i)



heap = MaxHeap([5,13,2,25,7,17,20,8,4])
print(heap.display())
heap.heapSort()
print(heap.display())