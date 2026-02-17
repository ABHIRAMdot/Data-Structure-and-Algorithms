# a = [1,2,3,4,5]

# def sum_of_array(ar):
#     if len(ar) == 0:
#         return 0
#     return ar[0] + sum_of_array(ar[1:])

# print(sum_of_array(a))

# s = "Hello"

# def reverse_string(st):
#     if len(st) == 1:
#         return st
    
#     return reverse_string(st[1:]) + st[0]

# print(reverse_string(s))


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None

# class Doubly_LL:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def print_Dll(self):
#         if self.head is None:
#             print("DLL is empty")
#             return
#         n = self.head
#         while n:
#             print(n.data, "-->", end=" ")
#             n = n.next

#     def add_end(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#             return
#         n = self.head
#         while n.next:
#             n = n.next
#         n.next = new_node
#         new_node.prev = n

#     def find_mid(self):
#         s = self.head
#         f = self.head

#         while f and f.next:
#             s = s.next
#             f = f.next.next
        
#         return s.data
    
#     def reverse_DLL(self):
#         n = self.head

#         self.tail = self.head

#         while n:
#             n.next, n.prev = n.prev, n.next
#             if n.prev is None:
#                 self.head = n
#             n = n.prev



# d = Doubly_LL()

# d.add_end(10)
# d.add_end(20)
# d.add_end(30)
# d.add_end(40)
# d.add_end(50)
# d.add_end(60)
# d.add_end(70)

# # print(d.find_mid())
# d.reverse_DLL()
# d.print_Dll()









# ar = [1, 3, 5, 7, 9, 11]

# def find_target(ar, target):
#     l = 0
#     r = len(ar) -1

#     while l <= r:
#         mid = (l + r) //2
#         if ar[mid] == target:
#             return mid
#         if ar[mid] > target:
#             r = mid - 1
#         else:
#             l = mid + 1

# print(find_target(ar, 7))


ar = [2, 4, 4, 4, 5, 6]

def find_first_and_last_of_target_number(ar, target):

    def first_ocurence(ar, target):
        l = 0
        r = len(ar) - 1
        first = -1

        while l <= r:
            mid  = (l + r) // 2
            if ar[mid] == target:
                first = mid
                r = mid - 1
            elif ar[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return first
    
    def last_occurence(ar, target):
        l = 0
        r = len(ar) - 1
        last = -1

        while l <= r:
            mid = (l + r) // 2
            if ar[mid] == target:
                last = mid 
                l = mid + 1
            elif ar[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return last
    
    return [first_ocurence(ar, target), last_occurence(ar, target)]


print(find_first_and_last_of_target_number(ar, 4))
    

