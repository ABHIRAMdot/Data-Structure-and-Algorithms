import heapq

def kth_largest(arr, k):
    min_heap = []

    for i in arr:
        heapq.heappush(min_heap, i)

        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return min_heap[0]

arr = [10, 4, 25, 20, 15]
k = 3

# print(kth_largest(arr, k))


from collections import Counter

def top_k_frequent(arr, k):
    freq = Counter(arr)

    min_heap = []

    for num, count in freq.items():
        heapq.heappush(min_heap, (count, num))

        if len(min_heap) > k:
            heapq.heappop(min_heap)

    result = []

    for count, num in min_heap:
        result.append(num)

    return result

nums = [1,1,1,2,2,3,3,3]
k = 2

print(top_k_frequent(nums, k))

