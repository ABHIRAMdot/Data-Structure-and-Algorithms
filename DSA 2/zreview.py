# input = ['m', 'a', 'z', 'b', 'k', 'e', 'q', 'c']
# # output = ['a', 'b', 'c', 'e', 'k', 'm', 'q', 'z']



# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class StackUsingLL:
#     def __init__(self):
#         self.top = None
    
#     def isEmpty(self):
#         return self.top is None
    
#     def push(self, val):
#         new_node = Node(val)
#         new_node.next = self.top
#         self.top = new_node
    
#     def pop(self):
#         if self.isEmpty():
#             print("Stack Underflow")
#             return
#         value = self.top.data
#         self.top = self.top.next
#         return value



# (()){} True

# ({[}) False

# ({[]}) True

# ({[]} False
 

# def valid_para(s):
#     stack = []

#     mapping = {
#         ')' : '(',
#         '}' : '{',
#         ']' : '['
#     }

#     for i in s:
#         if i in '({[':
#             stack.append(i)
#         else:
#             if not stack:
#                 return False
#             top = stack.pop()

#             if mapping[i] != top:
#                 return False
#     return len(stack) == 0


# print(valid_para("({[]}"))


class Queue:
    def __init__(self, size):
        self.size = size
        self.arr = [None] * size
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        return self.front == -1 or self.front > self.rear
    
    def isFull(self):
        return self.rear == self.size -1
    
    def enqueue(self, val):
        if self.isFull():
            print("Queue OverFlow")
            return
        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.arr[self.rear] = val

    def dequeue(self):
        if self.isEmpty():
            print("Queue Underflow")
            return
        value = self.arr[self.front]
        self.front += 1

        return value
    
    def display(self):
        
        for i in range(self.front, self.rear + 1):
            print(self.arr[i], end=" ")
        print()
    
q = Queue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("poped", q.dequeue())

q.display()

