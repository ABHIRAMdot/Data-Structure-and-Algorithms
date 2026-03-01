def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list

    # return "".join(sorted_list)


# s = [5,2,8,1,3]
# print(merge_sort('dcba'))

# input = ['m', 'a', 'z', 'b', 'k', 'e', 'q', 'c']
# print(merge_sort(input))

#---------------------------------


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



def merge_sort(head):
    if head is None or head.next is None:
        return head
    
    middle = getMiddle(head)
    next_to_middle = middle.next
    middle.next = None      #pliting by changing to None

    left = merge_sort(head)
    right = merge_sort(next_to_middle)

    sorted_list = sorted_merge(left, right)

    return sorted_list

def getMiddle(head):
    if head is None:
        return head
    
    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return  slow

def sorted_merge(a, b):
    if a is None:
        return b
    if b is None:
        return a
    
    if a.data <= b.data:
        result = a
        result.next = sorted_merge(a.next, b)
    else:
        result = b
        result.next = sorted_merge(a, b.next)

    return result

def print_list(head):
    n = head
    while n:
        print(n.data, end="-->")
        n = n.next
    print("None")

head = None

head = Node(30)
head.next = Node(10)
head.next.next = Node(20)


# print_list(head)

# head = merge_sort(head)

# print_list(head)

#-----------------------------------

#sort array of students by their marks using merge sotrt

students = [
    {"name": "Abhi", "marks": 85},
    {"name": "Ravi", "marks": 92},
    {"name": "John", "marks": 78}
]

def merge_sort_students(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort_students(left)
    right = merge_sort_students(right)

    return merge_students(left, right)

def merge_students(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i]["marks"] < right[j]["marks"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

# print(merge_sort_students(students))

#-----------------------------------------



