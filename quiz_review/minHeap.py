class MinHeap:
    def __init__(self, array = None):
        self.heap = array[:] if array else []
        if self.heap:
            self.build_heap()


    def left_child(self, i):
        return 2 * i + 1

    def right_child(self , i):
        return 2 * i + 2

    def parent(self, i):
        return (i - 1) // 2

    def heapify(self, i):
        smallest = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            # swap and recursively call the heapify method
            self.heap[smallest], self.heap[i] = self.heap[i], self.heap[smallest]
            self.heapify(smallest)


    def build_heap(self):
        n = len(self.heap)
        for i in range(n // 2 - 1, -1 ,-1):
            self.heapify(i)



    def insert_new(self, value):
        self.heap.append(value)
        index = len(self.heap) - 1

        while index > 0 and self.heap[index] < self.heap[self.parent(index)]:
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)



    def extract_minimum(self):
        if len(self.heap) == 0:
            return 


        if len(self.heap) == 1:
            return self.heap.pop()

        min_value = self.heap[0]
        self.heap[0] = self.heap.pop() # Swap with the last element
        self.heapify(0) # Fix the heap with the new root
        return min_value



    def display(self):
        return self.heap
    


heap = MinHeap([5,4,3,2,1])
heap.heapify(0)
print(heap.display())
print("Extracted min:", heap.extract_minimum())  # Should remove the largest element
print(heap.display())

        
        
        
        

        
        
            