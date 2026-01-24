class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class Linked_list:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("Linked List Head is Empty.")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->",  end=" ")
                n = n.ref


    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_after(self, data, x):
        n = self.head

        while n is not None:
            if x == n.data:
                break
            n = n.ref
        
        if n is None:
            print("Node is not present in LL")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_before(self, data, x):
        if self.head is None:
            print("Linked list is empty!")
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
        
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        
        if n.ref is None:
            print("Node not found!")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    
    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked list is not empty")



LL1 = Linked_list()

LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_end(100)
LL1.add_end(200)
LL1.add_end(300)
LL1.add_begin(30)
LL1.add_after(50, 300)
LL1.add_before(888, 200)
LL1.insert_empty(20000)
LL1.print_LL()




# Linked list wit explanation

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.ref = None

# class Liked_list:
#     def __init__(self):
#         self.head = None
    
#     def print_LL(self):
#         if self.head is None:
#             print("Linked List is Empty.")
#         else:
#             n = self.head
#             while n is not None:
#                 print(n.data)
#                 n = n.ref

#     def add_begin(self, data):
#         new_node = Node(data)
#         new_node.ref = self.head
#         self.head = new_node
    
#     def add_end(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#         else:
#             n = self.head
#             while n.ref is not None:
#                 n = n.ref
#             n.ref = new_node
            
    
#     def add_after(self, data, x):
#         n = self.head
#         while n is not None:
#             if x == n.data:
#                 break
#             n = n.ref
        
#     #in the above n.ref means the reference of node that cotaining x data.
#     # ie. if we found x in this node = (data(20) and ref(01234)) then loop  breaks from there, so the 'n.data= 20' and 'n.ref= 01234'.
#     # Now we can change the reference of the New Node to n.ref

#         if n is None:
#             print("Node is not present in Linked List")
#         else:
#             new_node = Node(data)
#             new_node.ref = n.ref
#             n.ref = new_node


#     def add_before(self, data, x):
#         if self.head is None:
#             print("Linked List is empty!")
#             return 
#         if self.head.data == x:    #if the x is to add at the beginning
#             new_node = Node(data)
#             new_node.ref = self.head
#             self.head = new_node

#             return
        
#         n = self.head
#         while n.ref is not None:  # means till the end of the linked list
#             if n.ref.data == x:   #the reference of previous node's data ie. pre =[10 | 02234]  next=[20 | 09888] then n.ref.data means - pre.02234.20 = that is 20.
#                 break
#             n = n.ref  # if not equal to 'x' then change n to that reference
        
#         if n.ref is None:
#             print("Node not fpund !")
        
#         else:
#             new_node = Node(data)  #create new node 
#             new_node.ref = n.ref   # assign n.ref that is the previous node's next ref.
#             n.ref = new_node      # then new node's reference to the previous node
    
    # def insert_empty(self, data):   #  This is to add a single node to an empt Linked list
    #     if self.head is None:
    #         new_node = Node(data)
    #         self.head = new_node
    #     else:
    #         print("Linked Listis Not Empty!")




    
# LL1 = Liked_list()
# LL1.add_begin(10)
# LL1.add_begin(20)
# LL1.add_end(100)
# LL1.add_after(50, 10)
# LL1.add_before(900, 100)
# LL1.print_LL()

#-----------------------------------