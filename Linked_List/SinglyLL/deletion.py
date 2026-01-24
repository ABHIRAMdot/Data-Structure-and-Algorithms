
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None
    
class Linked_list:
    def __init__(self):
        self.head = None

    def print_LL(self):
        n = self.head
        while n is not None:
            print(n.data)
            n = n.ref

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            print("Linked list is Empty")
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
    
    def delete_begin(self):
        if self.head is None:
            print("LL is empty unable to delete.")
        else:
            self.head = self.head.ref

    def delet_end(self):
        if self.head is None:
            print("unable to delete. Linked list is empty")
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:    
                n = n.ref
            n.ref = None
            
    def delete_any_value(self, x):
        if self.head is None:
            print("LL is empty")
            return
        if self.head.data == x:
            self.head = self.head.ref
        else:
            n = self.head
            while n.ref is not None:
                if n.ref.data == x:
                    break
                n = n.ref

            if n.ref is None:
                print("Node is not Present!")
            else:
                n.ref = n.ref.ref





            

ll = Linked_list()
ll.add_begin(10)
ll.add_end(20)
ll.add_end(30)
ll.add_end(40)

ll.delete_any_value(50)
# ll.delet_end()
# ll.delete_begin()
ll.print_LL()