class MaxHeap:
    def __init__(self):
        self.heap = []

    # Insert element
    def insert(self, val):
        self.heap.append(val)
        self.heapify_up(len(self.heap)-1)

    #heapify upward
    def heapify_up(self, index):   #index will be the next position that we are inserting in the heap
        parent = (index - 1) // 2  # here parent is the root(index or parent node)  of the new node 

        if index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self.heapify_up(parent)

    # remove maximum element
    def extract_max(self):
        if len(self.heap) == 0:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)

        return root
    
    #heapify downward
    def heapify_down(self, index):
        largest = index
        left = 2*index + 1
        right = 2*index + 2


        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify_down(largest)

    def print_heap(self):
        print(self.heap)


# h = MaxHeap()

# h.insert(10)
# h.insert(40)
# h.insert(30)
# h.insert(50)

# h.print_heap()
# print(h.extract_max())
# h.print_heap()



def build_max_heap(arr):
    n = len(arr)

    for i in range(n//2-1, -1 , -1): #  start from last non leaf's parent index and backwords
        heapify_down(arr, i, n)


def heapify_down(arr, index, size):
    largest = index

    left = 2*index + 1
    right = 2*index + 2

    if left < size and arr[left] > arr[largest]:
        largest = left

    if right < size and arr[right] > arr[largest]:
        largest = right

    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        heapify_down(arr, largest, size)



# arr = [10,40,30,50]
# build_max_heap(arr)
# print(arr)
