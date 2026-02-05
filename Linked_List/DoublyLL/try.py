class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Doubly_LL:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_DLL(self):
        if self.head is None:
            print("DLL is empty")
            return
        n = self.head
        while n:
            print(n.data, "-->", end=" ")
            n = n.next
    
    def print_reverse(self):
        print()
        if self.head is None:
            print("DLL is empty")
            return 
        # n = self.head
        n= self.tail
        # while n.next:
        #     n = n.next
        
        while n:
            print(n.data, "<--", end=" ")
            n = n.prev

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node 
        # n = self.head
        # while n.next:
        #     n = n.next
        # n.next = new_node
        # new_node.prev = n
        # self.tail = new_node
        
    def add_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def add_after(self, data, x):
        if self.head is None:
            print("DLL is empty")
            return
        n = self.head
        while n:
            if n.data == x:
                break
            n = n.next
        if n is None:
            print("node is not found")
        else:
            new_node = Node(data)
            new_node.next = n.next
            new_node.prev = n.prev
            if n.next is not None:
                n.next.prev = new_node
            else:
                self.tail = new_node
            n.next = new_node

    def add_before(self, data, x):
        if self.head is None:
            print("DLL is empty")
            return
        n = self.head
        while n:
            if n.data == x:
                break
            n = n.next

        if n is None:
            print("Node not found")
        else:
            new_node = Node(data)
            new_node.next = n
            new_node.prev = n.prev
            if n.prev is not None:
                n.prev.next = new_node
            else:
                self.head = new_node
            n.prev = new_node
    
    def delete_end(self):
        if self.head is None:
            print("DLL is already empty")
            return
        if self.head and self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
    def delete_begin(self):
        if self.head is None:
            print("DLL is already empty")
            return
        if self.head and self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None


dl =Doubly_LL()
dl.add_end(10)
dl.add_end(20)
dl.add_end(30)
dl.add_end(40)

# dl.add_begin(50)
dl.add_after(60, 30)
dl.add_before(70, 30)
dl.delete_end()
dl.delete_begin()
dl.print_DLL()
# dl.print_reverse()
