import heapq

def kth_largest(arr, k):
    min_heap = []

    for i in arr:
        heapq.heappush(min_heap, i)

        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return min_heap[0]

arr = [10, 4, 7, 20, 15]
k = 3

print(kth_largest(arr, k))