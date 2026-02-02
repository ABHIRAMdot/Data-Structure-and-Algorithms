
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.ref = None

# class Linked_List:
#     def __init__(self):
#         self.head = None

#     def print_LL(self):
#         if self.head is None:
#             print("Linked lsit is empty")
#             return
#         n = self.head
#         while n:
#             print(n.data,"-->", end=" ")
#             n = n.ref

#     def add_end(self,data):
#         if self.head is None:
#             new_node = Node(data)
#             self.head = new_node
#         else:
#             n = self.head
#             while n.ref:
#                 n = n.ref
            
#             new_node = Node(data)
#             n.ref = new_node

#     def remove_duplicates(self):
#         s = set()
#         n= self.head
#         prev = None
        
#         while n:
#             if n.data in s:
#                 prev.ref= n.ref
#             else:
#                 s.add(n.data)
#                 prev = n
#             n = n.ref

        


# l = Linked_List()
# l.add_end(1)
# l.add_end(2)
# l.add_end(3)
# l.add_end(1)
# l.add_end(2)
# l.add_end(3)

# l.remove_duplicates()
# l.print_LL()

s = input("Enter a string \n")

f = {}


for i in s:
    if i in f:
        f[i] += 1
    else:
        f[i] = 1

for i in s:
    if f[i] ==1:
        print(i)
        break

# for i in s:
#     f[i] = f.get(i, 0) + 1    #it gives the count of i or zero and + 1

# for i in s:
#     if f[i] == 1:
#         print(i)
#         break



