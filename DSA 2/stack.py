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