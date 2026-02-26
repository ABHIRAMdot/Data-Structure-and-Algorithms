
# Simple/Linear queue using array

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
    
    def enqueue(self, value):
        if self.isFull():
            print("Queue Overflow")
            return
        if self.front == -1:
            self.front = 0

        self.rear += 1
        self.arr[self.rear] = value

    def dequeue(self):
        if self.isEmpty():
            print("Queue Underflow")
            return
        
        value = self.arr[self.front]
        self.front += 1
        return value
    
    def display(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        for i in range(self.front, self.rear +1):
            print(self.arr[i], end=" ")
        print()

q = Queue(5)

# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)
# q.enqueue(40)
# q.enqueue(50)

# q.dequeue()
# q.enqueue(60)
# q.display()

#-----------------------------------------

# Queue using Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLL:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def isEmpty(self):
        return self.front is None
    
    def enqueue(self, val):
        new_node = Node(val)

        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.isEmpty():
            print("Queue Underflow")
            return
        value = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return value
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.front.data
    
    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    
# q = QueueLL()
# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)

# q.dequeue()
# print(q.peek())
# q.display()

#-------------------------------------------

class QueueUsingStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, val):
        self.stack1.append(val)


    def dequeue(self):
        if not self.stack1:
            print("Queue Underflow")
            return
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        value = self.stack2.pop()

        while self.stack2:
            self.stack1.append((self.stack2.pop()))
        
        return value
    
    def peek(self):
        if not self.stack1:
            return None
        
        return self.stack1[0]
    

# q = QueueUsingStack()
# q.enqueue(19)
# q.enqueue(20)
# q.enqueue(21)

# print(q.dequeue())
# print(q.peek())

#------------------------------------------

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.arr = [None] * size
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        return self.front == -1
    def isFull(self):
        return (self.front ==(self.rear +1) % self.size)
    
    def enqueue(self, val):
        if self.isFull():
            print("Queue Overflow")
            return
        if self.isEmpty():
            self.front = self.rear = 0

        else:
            self.rear = (self.rear + 1) % self.size

        self.arr[self.rear] = val

    def dequeue(self):
        if self.isEmpty():
            print("Queue Underflow")
            return
        value = self.arr[self.front]

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        
        return value
    
    def display(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        
        i = self.front
        while True:
            print(self.arr[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()

q = CircularQueue(5)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

q.dequeue()

q.enqueue(4)
q.display()