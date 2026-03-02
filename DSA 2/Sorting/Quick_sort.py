def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr)//2]
    left = [i for i in arr if i < pivot]
    middle = [i for i in arr if i == pivot]
    right = [i for i in arr if i > pivot]

    return quick_sort(left) + middle + quick_sort(right)


ar = [10, 7, 8, 9, 1, 5]

# print(quick_sort(ar))


#-------------------------------------------------

#quick sort inplace sorting

def quick_sort(arr, low, high):
    if low < high:
        pivot_idx = partition(arr, low, high)
        quick_sort(arr, low, pivot_idx -1)
        quick_sort(arr, pivot_idx + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i + 1


arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr)-1)
print(arr)
#--------------------------------------------