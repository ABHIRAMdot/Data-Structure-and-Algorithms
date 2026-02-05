class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class singly_ll:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("linked list is empty")
            return 
        n = self.head
        while n:
            print(n.data, "-->", end=" ")
            n = n.ref
    
    def add_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        n = self. head
        while n.ref:
            n = n.ref
        n.ref = new_node
    
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def find_mid(self):
        s = self.head
        f =self.head
        
        while f and f.ref:
            s = s.ref
            f = f.ref.ref
        
        return s.data
    
    def reverse_ll(self):
        prev = None
        cur = self.head

        while cur:
            temp = cur.ref
            cur.ref = prev
            prev = cur

            cur = temp
        self.head = prev

    def remove_duplicates(self):
        print()
        n = self.head
        while n and n.ref:
            if n.data == n.ref.data:
                n.ref = n.ref.ref
            else:
                n = n.ref

    def remove_dup_from_unsorted(self):
        print()
        seen = set()
        prev = None
        n = self.head

        while n:
            if n.data in seen:
                prev.ref = n.ref
            else:
                seen.add(n.data)
                prev = n
            n = n.ref

    def add_after_node(self, data, x):
        if self.head is None:
            print("LL is empty")
            return
        
        n = self.head
        while n:
            if n.data == x:
                break
            n= n.ref
        
        if n is None:
            print("node not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_before_node(self, data, x):
        if self.head is None:
            print("LL is None")
            return
        
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        
        n = self.head
        while n.ref:
            if n.ref.data ==x:
                break
            n = n.ref
        if n.ref is None:
            print("Node not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def remove_middle(self):
        s = self.head
        f = self.head
        prev = None
        while f and f.ref:
            prev = s
            s = s.ref
            f = f.ref.ref
        prev.ref = s.ref

    def delete_end(self):
        if self.head is None:
            print("LL is empty")
            return
        if self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref:
                n = n.ref
            n.ref = None
    
    def delete_begin(self):
        if self.head is None:
            print("LL is empty")
        else:
            self.head = self.head.ref
    
    def delete_any(self, x):
        if self.head is None:
            print("LL is empty")
            return 
        if self.head.data == x:
            self.head = self.head.ref
            return
        n = self.head
        while n:
            if n.ref.data == x:
                break
            n= n.ref
        
        if n is None:
            print("Node not found")
        else:
            n.ref = n.ref.ref

    def array_to_LL(self, ar):
        for i in ar:
            self.add_end(i)

    
l = singly_ll()
# l.add_end(10)
# l.add_end(40)
# l.add_end(20)
# l.add_end(40)
# l.add_end(30)
# l.add_end(40)
# l.add_end(20)

l.add_end(10)
l.add_end(20)
l.add_end(30)
l.add_end(40)

l.delete_any(40)
# l.add_after_node(50, 10)
# l.add_before_node(60, 50)

# l.add_begin(5)

# print(l.find_mid())
# l.remove_middle()
# l.reverse_ll()


# l.delete_end()

l.print_LL()
# l.remove_duplicates()
# l.remove_dup_from_unsorted()
# l.print_LL()