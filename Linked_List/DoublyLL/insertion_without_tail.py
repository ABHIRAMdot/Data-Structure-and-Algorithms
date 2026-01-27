
class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None
        

class DoulyLL:
    def __init__(self):
        self.head = None

    def print_F_DL(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.nref
    
    def print_reverse_DL(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.pref

    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked list is not Empty")


    def add_begin(self, data):
        new_node = Node(data) 
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node
    
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head   
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

    def add_after(self, data, x):
        if self.head is None:
            print("Linked List is empty.")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("Node is not found")
            else:
                new_node = Node(data)
                new_node.nref = n.nref                
                new_node.pref = n
                if n.nref is not None:     # if the the data position is in last/tail there will not be nextreference and its previous reference it will be null so check here. 
                    n.nref.pref = new_node
                n.nref = new_node
    
    def add_before(self, data, x):
        if self.head is None:
            print("Linked list is Empty")
        else:
            n = self.head
            while n  is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("Node is not found")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:      #means if its not at the beginning
                    n.pref.nref = new_node
                else:
                    self.head = new_node     # if we are adding at the beginning we have to change the head to new_node.
                n.pref = new_node
                
    
    def delete_begin(self):
        if self.head is None:
            print("Linked list is Empty!")
            return
        if self.head.nref is None:
            self.head = None
            print("Linked list is empty after deleting the node.")
        else:
            self.head = self.head.nref
            self.head.pref = None

    def delete_end(self):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.nref is None:
            self.head = None
            print("LL is empty after deleting the Node")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None

    def delete_any(self, x):
        if self.head is None:
            print("LL is empty")
            return
        if self.head.nref is None:
            if self.head.data == x:
                self.head = None
                print("after deleting x lL is empty")
            else:
                print("x is not found in this LL")
            return
        if self.head.data == x:
            self.head = self.head.nref
            self.head.pref = None
            return

        n = self.head
        while n.nref is not None:
            if n.data == x:
                break
            n = n.nref

        if n.nref is not None:
            n.nref.pref = n.pref
            n.pref.nref = n.nref

        else:
            if n.data == x:
                n.pref.nref = None
            else:
                print("x is not present in DLL")

    def insert_before_index(self, data, pos):
        new_node = Node(data)
        if pos == 0:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node
            return
        n = self.head
        index = 0
        while n and index != pos -1:
            n = n.nref
            index += 1

        if not n or not n.nref:
            print("indx out of range")
            return
        new_node.nref = n.nref
        new_node.pref = n
        n.nref.pref = n
        n.nref = new_node 






dl1 = DoulyLL()
dl1.add_begin(10)
dl1.add_end(20)
dl1.add_after(30, 20)
dl1.add_before(50, 20)
# dl1.delete_end()

# dl1.delete_begin()
# dl1.delete_any(10)
dl1.insert_before_index(80, 4)
dl1.print_F_DL()

# dl1.print_reverse_DL()
