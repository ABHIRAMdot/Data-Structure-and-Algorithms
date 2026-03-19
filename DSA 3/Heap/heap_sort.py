def heapify(arr, index, size):
    largest = index
    left = 2*index + 1
    right = 2*index + 2

    if left < size and arr[left] > arr[largest]:
        largest = left
    
    if right < size and arr[right] > arr[largest]:
        largest = right 

    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        heapify(arr, largest, size)

    
def heap_sort(arr):
    n = len(arr)

    for i in range(n//2 -1, -1, -1):   # for heapifying from the last none leaf node
        heapify(arr, i, n)

    for i in range(n-1, 0, -1):   # if len(arr) == 5 then range becomes 4,3,2,1 stops before 0
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)    # it will return arguments like first- heapify(arr, 4, 0) then index 4 will be ignore in heapify.


# arr = [10, 40, 30, 50]

# heap_sort(arr)

# print(arr)
        
#------------------------------------------

# Find kth largest
import  heapq

def took_k_largest(arr, k):
    min_heap = []

    for num in arr:
        heapq.heappush(min_heap, -num)

        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return -min_heap[0]

arr = [10, 4, 7, 20, 2,15]
k = 3

print(took_k_largest(arr, k))
