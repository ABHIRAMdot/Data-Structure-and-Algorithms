# Stack using Array

# class Stack:
#     def __init__(self, size):
#         self.size = size
#         self.arr = [None] * size
#         self.top = -1        #stack pointer

#     def isEmpty(self):
#         return self.top == -1
    
#     def isFull(self):
#         return self.top == self.size -1
    
#     def push(self, value):
#         if self.isFull():
#             print("Stack Overflow")
#             return
#         self.top += 1
#         self.arr[self.top] = value

#     def pop(self):
#         if self.isEmpty():
#             print("Stack underflow")
#             return 
#         value = self.arr[self.top]
#         self.top -= 1
#         return value
    
#     def peek(self):
#         if self.isEmpty():
#             print("Stack is Empty")
#             return
#         return self.arr[self.top]
    

# s = Stack(3)
# s.push(10)
# s.push(20)
# s.push(30)
# # s.pop()
# print(s.peek())


# class Stack:
#     def __init__(self, size):
#         self.size = size
#         self.arr = [None] * size
#         self.top = -1

#     def isEmpty(self):
#         return self.top == -1
    
#     def isFull(self):
#         return self.top == self.size -1
    
#     def push(self, value):
#         if self.isFull():
#             print("Stack Overflow")
#             return
#         self.top += 1
#         self.arr[self.top] = value
        
    
#     def pop(self):
#         if self.isEmpty():
#             print("Stack underflow")
#             return 
#         value = self.arr[self.top]
#         self.top -= 1
#         return value
    
#     def peek(self):
#         if self.isEmpty():
#             print("Stack is Empty")
#             return
#         return self.arr[self.top]
    
# s = Stack(3)

# s.push(2)
# s.push(3)
# s.push(4)
# print(s.pop())
# print(s.peek())



# Stack using Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
    
    def isEmpty(self):
        return self.top is None
    
    def push(self, val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
            return
        value = self.top.data
        self.top = self.top.next
        return value
    
    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")
            return
        
        return self.top.data

    
# s = Stack()
# s.push(222)
# s.push(444)
# s.push(555)

# print(s.pop())
# print(s.peek())

#-------------------------------------

# Reverse a string using Stack


class Stack:
    def __init__(self, size):
        self.arr = [None] * size
        self.top = -1
        
    def push(self, val):
        self.top += 1
        self.arr[self.top] = val
        return
    
    def pop(self):
        value = self.arr[self.top]
        self.top -= 1
        return value
        
def reverse(s):
    stack = Stack(len(s))
    
    for i in s:
        stack.push(i)
    
    rev = ""
    while stack.top != -1:
        rev += stack.pop()
    
    return rev
    
# print(reverse("abc"))

#------------------------

#valid paranthesis

def valid_para(s):
    stack = []
    
    mapping = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }
    
    for i in s:
        if i in '({[':
            stack.append(i)
        else:
            if not stack:
                return False
            
            top = stack.pop()
            if mapping[i] != top:
                return False
    
    return len(stack) == 0
    

# print(valid_para("{[])}"))

#-------------------------------------

# Stack using Queue

from collections import deque

class StackUsingQueue:
    def __init__(self):
        self.q = deque()

    def push(self, val):
        self.q.append(val)

        for _ in range(len(self.q) -1):
            self.q.append(self.q.popleft())

    
    def pop(self):
        return self.q.popleft()
    
    def top(self):
        return self.q[0]
    
    def empty(self):
        return len(self.q) ==0
    
    def display(self):
        print(list(self.q))
    
# q = StackUsingQueue()

# q.push(10)
# q.push(20)
# q.push(30)

# q.pop()
# q.push(40)
# q.display()

#----------------------------

class MySTack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)

        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        value = self.stack.pop()

        if value == self.min_stack[-1]:
            self.min_stack.pop()

        return value
    
    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.min_stack[-1]
    
# s = MySTack()
# s.push(7)
# s.push(3)
# s.push(5)
# s.push(2)

# s.pop()
# s.pop()

# print(s.top())
# print(s.getMin())


#-----------------------------------------

def deleteMiddle(stack, k):
    if k == 1:
        stack.pop()
        return
    
    temp = stack.pop()
    
    deleteMiddle(stack, k - 1)

    stack.append(temp)

def removeMiddle(stack):
    n = len(stack)
    k = n// 2+1
    deleteMiddle(stack, k)


s = [1,2,3,4,5,6]

# removeMiddle(s)

# print(s)


# sort stack using recursion only

def sort_stack(stack):
    if not stack:
        return
    
    top = stack.pop()
    sort_stack(stack)
    insert_sorted(stack, top)
    

def insert_sorted(stack, element):
    if not stack or stack[-1] <= element:
        stack.append(element)
        return
    
    temp = [3, 1, 4, 2]
    insert_sorted(stack, element)
    stack.append(temp)


stack = [3,1,4,2]

sort_stack(stack)
print(stack)