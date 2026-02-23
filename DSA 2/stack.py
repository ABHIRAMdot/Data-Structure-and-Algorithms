# s = []
# s.append('https://www.cnn.com/')
# s.append('https://www.cnn.com/world')
# s.append('https://www.cnn.com/india')
# s.append('https://www.cnn.com/china')

# print(s.pop())

class Stack:
    def __init__(self, size):
        self.size = size
        self.arr = [None] * size
        self.top = -1        #stack pointer

    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top == self.size -1
    
    def push(self, value):
        if self.isFull():
            print("Stack Overflow")
            return
        self.top += 1
        self.arr[self.top] = value

    def pop(self):
        if self.isEmpty():
            print("Stack underflow")
            return 
        value = self.arr[self.top]
        self.top -= 1
        return value
    
    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")
            return
        return self.arr[self.top]
    

s = Stack(3)
s.push(10)
s.push(20)
s.push(30)
# s.pop()
print(s.peek())