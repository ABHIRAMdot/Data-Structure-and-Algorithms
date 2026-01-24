
class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None
        

class DoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_F_DL(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.nref
    
    def print_reverse_DL(self):
        print()
        if self.head is None:
            print("Linked list is empty")
        else:
            n= self.tail
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.pref

    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node
        else:
            print("Linked list is not Empty")


    def add_begin(self, data):
        new_node = Node(data) 
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node
    
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.nref = new_node
            new_node.pref = self.tail
            self.tail = new_node

    def add_after(self, data, x):
        if self.head is None:
            print("Linked List is Empty.")
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.nref
            if n is None:
                print("Node is not found")
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref is not None:
                    n.nref.pref = new_node
                else:
                    self.tail = new_node
                n.nref = new_node 

    def add_before(self, data, x):
        if self.head is None:
            print("Linked List is Empty!")
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.nref
            
            if n is None:
                print("Node is not Found!")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                    
                n.pref = new_node

    def delete_begin(self):
        if self.head is None:
            print("Linked list is Empty")
            return
        if self.head.nref is None:
            self.head = None
            self.tail = None
            print("Node removed LL is empty now")
        else:
            self.head = self.head.nref
            self.head.pref = None

    def delete_end(self):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.nref is None:
            self.head = None
            self.tail = None
            print("node removed LL is Empty now")
        else:
            self.tail = self.tail.pref
            self.tail.nref = None

    def delete_any(self, x):
        if self.head is None:
            print("Linked list is empty")
            return
        # if there is only one node
        if self.head.nref is None:
            if self.head.data == x:
                self.head = None
                self.tail = None
                print("DL is empty after deleting x")
            else:
                print("can't find the node x")
            return
        # if x is in the beginning
        if self.head.data == x:
            self.head = self.head.nref
            self.head.pref = None
            return 

        n = self.head
        #traverse tho=rough all nodes to find x
        while n is not None:
            if n.data == x:
                break
            n = n.nref
        # if x is not found in LL (ie. n= None)
        if n is None:
            print("Node not found ")
            return
        # if x is found in LL, then check if the x is in the end/tail
        if n == self.tail:
            self.tail = n.pref
            self.tail.nref = None
        
        # if it not at the end then it should be in inbetween.
        else:
            n.pref.nref = n.nref
            n.nref.pref = n.pref
        

        # alternative
        
        # while n.ref is not None:
        #     if x == n.data:
        #         break
        #     n = n.ref

        # # if the x is found before the end/tail
        # if n.nref is not  None:
        #     n.nref.pref = n.pref
        #     n.pref.nref = n.nref  

        #  # if x is in the end   
        # else:
        #     if n.data == x:
        #         self.tail = n.pref                
        #         n.pref.nref = None



            

            


dl1 = DoublyLL()
# dl1.insert_empty(100)

dl1.add_begin(10)
dl1.add_end(20)
dl1.add_after(30, 20)
dl1.add_before(40, 10)
# dl1.delete_begin()
# dl1.delete_end()
dl1.delete_any(40)

dl1.print_F_DL()
dl1.print_reverse_DL()
