class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Singly_LL:
    def __init__(self):
        self.head = None

    def print_LL(self):
        n = self.head
        while n :
            print(n.data, "-->", end=" ")
            n = n.next

    def add_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def add_end(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            n = self.head
            while n.next:
                n = n.next
            new_node = Node(data)
            n.next = new_node

    def add_after(self, data, x):
        n = self.head
        while n:
            if n.data == x:
                break
            n = n.next
        
        if n is None:
            print("LL is empty")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    def add_before(self, data, x):
        if self.head is None:
            print("LL is empty")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.next = self.head.next
            self.head = new_node
            return
        n = self.head
        while n.next:
            if n.next.data == x:
                break
            n = n.next

        if n.next:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node
        else:
            if n.data == x:
                new_node = Node(data)
                n.next = new_node

    def delete_begin(self):
        if self.head is None:
            print("LL is empty")
        self.head = self.head.next
    
    def delete_end(self):
        if self.head is None:
            print("LL is empty")
        elif self.head.next is None:
            self.head = self.head.next
        else:
            n = self.head
            while n.next.next:
                n = n.next
            
            n.next = None
            
    def delete_any(self, x):
        if self.head is None:
            print("LL is  empty")
            return
        if self.head.data == x:
            self.head = self.head.next
            return
        n = self.head
        while n.next:
            if n.next.data ==x:
                break
            n = n.next
        if n.next is None:
            print("Node not found")
        else:
            n.next = n.next.next       

    def array_to_lst(self,arr):
        if arr is None:
            print("array is empty")
            return
        for i in arr:
            self.add_end(i)

    def remove_duplicate(self):
        n = self.head
        while n.next:
            if n.data == n.next.data:
                n.next = n.next.next
            else:
                n = n.next






L = Singly_LL()
# L.add_begin(10)  
# # L.add_begin(5)
# L.add_end(20)
# L.add_after(30, 20)

# L.add_before(5,30)
# # L.delete_begin()
# # L.delete_end()
# L.delete_any(10)
ar = [10,10,10,20,30,30,40]
L.array_to_lst(ar)
L.remove_duplicate()
L.print_LL()