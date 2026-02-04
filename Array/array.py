# ar = [1,2,3,4,5]

# s = 0
# e = len(ar) -1

# while s < e:
#     ar[s], ar[e] = ar[e], ar[s]
#     s +=1
#     e -= 1

# print(ar)
#-------------------------------------

# m = [[1, 2], [3, 4], [5, 6]]

# f = []

# for i in m:
#     for j in i:
#         f .append(j)

# print(f)

#---------------------------------------

##bubble sort
# arr = [5, 1, 4, 2, 8]

# n = len(arr)

# for i in range(n):
#     for j in range(0, n-i-1):
#         if arr[j] > arr[j + 1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]


# print(arr)

#----------------------------------------------------

#binery search

# arr = [2, 4, 6, 8, 10, 12]

# target = 10

# low = 0
# high = len(arr) - 1

# while low <= high:
#     mid = (low + high) // 2

#     if target == arr[mid]:
#         print("Target found at index,", mid)
#         break
#     elif target > arr[mid]:
#         low = mid + 1

#     else:
#         high = mid - 1
    # return -1

#-----------------------------------------------------
# arr = [1, 2, 2, 3, 1, 4, 2]

# freq = {}

# for i in arr:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1

# print(freq) 

#-----------------------------------------------------

# arr = [1,2,3,4,6]

# sum = 0
# count = 0

# for i in arr:
#     if i %2 == 0:
#         sum += i
#         count += 1

# if sum == 0:
#     print("No even numbers")
# else:
#     avg = sum / count
#     print("average of even numbers", avg)

#-------------------------------------------------------

##second largest
arr = [5,2,7,4,6,1]

def second_largest(arr):
    f = 0
    s = 0

    for i in arr:
        if i > f:
            s = f
            f = i
        elif i > s and i < f:
            s = i
    return s

# print(second_largest(arr))

#------------------------------------------------------------
##third largest
def third_largest(arr):
    first = second = third = 0

    for i in arr:
        if i > first:
            third = second
            second = first
            first = i

        elif i > second and i != first:
            third = second
            second = i
        elif i > third and i != second and i != first:
            third = i

    return third

# print(third_largest(arr))

#--------------------------------------------------------------

#find minimum in sorted rotated
arr = [6,7,1,2,3,4,5]
def find_min(arr):
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = (low + high) // 2
        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid

    return arr[low]

# print(find_min(arr))

#--------------------------------------------------
def last_occurrence(arr, target):
    l, r = 0, len(arr)-1
    res = -1
    while l <= r:
        mid = (l+r)//2
        if arr[mid] == target:
            res = mid
            l = mid + 1
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return res

# print(last_occurrence([1,2,3,1,2,3,4], 4))

#-------------------------------------------------

