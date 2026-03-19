class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self.heapify_up(len(self.heap)-1)

    def heapify_up(self, index):
        parent = (index - 1) // 2

        if index > 0 and self.heap[parent] > self.heap[index]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self.heapify_up(parent)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)

        return root
    
    def heapify_down(self, index):
        smallest = index
        left = 2*index + 1
        right = 2*index + 2

        if left < len(self.heap) and self.heap[left] < self.heap[smallest] :
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify_down(smallest)

    # def print_heap(self):
    #     print(self.heap)


h = MinHeap()

h.insert(10)
h.insert(40)
h.insert(30)
h.insert(50)

h.print_heap()
