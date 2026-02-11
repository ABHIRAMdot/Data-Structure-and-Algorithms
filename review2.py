# s = "abc123def45"

# lst = []

# for i in s:
#     if i.isdigit():
#         lst.append(int(i))

# print(lst)

# s1 = []

# for i in s:
#     if '0' <= i <= '9':
#         s1.append(i)

# print(''.join(s1))

#---------------------------------

# s = "abc 123 xyz"
# s = " ".join(i[::-1] for i in st.split())
# st = list(s)
# l = len(st) -1
# lef = 0

# for i in range(len(s)):
#     if i == l or s[i]  == ' ':
#         left, right = lef, i - 1
#         while left < right:
#             st[left], st[right] = st[right], st[left]
#             left += 1
#             right -= 1
#         lef = i + 1

#-----------------------------------------------------------

# s1 = ""
# word = ""


# for i in range(len(s)):
#     if s[i] != ' ' and i != len(s)-1:
#         word += s[i]
        
#     else:
#         for  j in range(len(word)-1, -1, -1):
#             s1+=word[j]
#         s1+= s[i]
#         word = ""

# print(''.join(s1))

#-------------------------------------------
# input = [1,0,2,0,3,0,4]
# count = 0


# for i in input:
#     if i == 0:
#         count +=1
#         input.pop(i)
    
# if count>0:
#     for i in range(count + 1):
#         input.append(0)
    


# print(input)


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None

# class Doubly_LL:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def print_DLL(self):
#         if self.head is None:
#             print("Linked List is Empty")
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
#         new_node.prev = n
#         n.next = new_node
#         self.tail = new_node     

#     def palindrom(self):
#         f = self.head
#         l = self.tail

#         while f:
#             if f.data != l.data:
#                 return False
#             f = f.next
#             l = l.prev
#         return True


# dl = Doubly_LL() 
# dl.add_end(10)
# dl.add_end(20)
# dl.add_end(20)
# dl.add_end(10)




# dl.print_DLL()  
# print()
# print(dl.palindrom())



input = 123

def sum_of_digits(s):
    a = str(s)

    if len(a) == 1:
        return int(a)
    
    return int(a[0]) + sum_of_digits(int(a[1:]))

# print(sum_of_digits(123))

# ---------------------------------------

def sum_of_digits(n):

    if n == 0:
        return 0
    
    return n % 10 + sum_of_digits(n // 10)

# print(sum_of_digits(123))

#--------------------------------------------------


# a = [1,2,3,4,5]

# def find_element(a, target):
#     l = 0
#     r = len(a) 

#     while l < r:
#         mid = (l + r) // 2
#         if a[mid] == target:
#             return mid
#         if a[mid] < target:
#             l = mid + 1
#         else:
#             r = mid

#     return mid

# print(find_element(a, ))

#----------------------------------------

# input = [1,0,2,0,3,0,4]
# s = []

# pos = 0

# for i in input:
#     if i != 0:
#         s.append(i)
#     else:
#         pos += 1

# for i in range(pos):
#     s.append(0)

# print(s)

# moving zeros to end without an extra list *
nums = [0,1,0,3,12]

n = len(nums)
pos = 0

for i in range(n):
    if nums[i] != 0:
        nums[pos], nums[i] = nums[i], nums[pos]
        pos +=1

# print(nums)
#------------------------------------------------------


# s = 123
# digit_sum = 0

# while s > 0:
#     temp = s % 10
#     digit_sum += temp
#     s //= 10

# print(digit_sum)



