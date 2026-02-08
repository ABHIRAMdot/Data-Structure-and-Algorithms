
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
            print(n.data, "-->", end=" ")
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
            if n.data == x:
                break
            n = n.ref
        
        if n is None:
            print("Linked list is empty")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_before(self, data, x):
        if self.head is None:
            print("LL is empty")
            return
        if self.head.data == x:
            self.add_begin(data)
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        
        if n.ref is not None:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
        else:
            if n.data == x:
                self.add_end(data)
            else:
                print("node not found")




    
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

    def array_to_all(self, arr):
        for value in arr:
            self.add_end(value)

    def insert_after_index(self, data, pos):
        
        new_node = Node(data)
        index = 0
        n = self.head
        while n and index != pos:
            n = n.ref
            index += 1
        if not n:
            print("Index out of range")
            return

        
        new_node.ref = n.ref
        n.ref = new_node

    def insert_before_index(self, data, pos):
        new_node = Node(data)

        if pos == 0:
            new_node.ref = self.head
            self.head = new_node
            return
        
        n = self.head
        index = 0
        while n and index != pos -1:
             n = n.ref
             index += 1
        
        if not n or not n.ref:
            print("index out of range")
            return
        
        new_node.ref = n.ref
        n.ref = new_node




    def remove_duplicates_sorted(self):
        curr = self.head

        while curr and curr.ref:
            if curr.data == curr.ref.data:
                curr.ref = curr.ref.ref
            else:
                curr =curr.ref
                
    def remove_duploicates_unsorted(self):
        seen = set()
        curr = self.head
        prev = None

        while curr and curr.ref:
            if curr.data in seen:
                prev.ref = curr.ref  #delete curr
            else:
                seen.add(curr.data)
                prev = curr
            
            curr = curr.ref


    def kth_remove_end(self, n):
        dummy = Node(0)
        dummy.ref = self.head

        slow = dummy
        fast = dummy
        for _ in range(n + 1):
            if fast is None:
                return
            fast = fast.ref

        while fast:
            slow = slow.ref
            fast = fast.ref
        
        slow.ref = slow.ref.ref

        self.head = dummy.ref

    def remove_last_occurrence(self, x):
        prev = None
        cur = self.head

        last_prev = None
        last_node = None

        while cur:
            if cur.data == x:
                last_prev = prev
                last_node = cur
            prev = cur
            cur = cur.ref
        
        if last_node is None:
            print("no match found")
            return
        if last_prev is None:
            self.head = self.head.ref
        else:
            last_prev.ref = last_node.ref

    def remove_nth_node_end(self, k):
        count = 0
        cur = self.head

        while cur:
            count +=1
            cur = cur.ref
        
        if k > count:
            print("Invalind position")
            return
        if k == count:
            self.head = self.head.ref
            return
        cur = self.head
        for _ in range(count - k - 1):
            cur = cur.ref
        cur.ref = cur.ref.ref





a = [11,22,33,44,55]
            

ll = Linked_list()
ll.add_begin(10)
ll.add_end(20)
ll.add_end(30)
ll.add_end(40)

# ll.delete_any_value(11)
# ll.delet_end()
# ll.delete_begin()

# ll.array_to_all(a)
# ll.insert_after_index(70, 0)
ll.kth_remove_end(2)
ll.print_LL()



# LL = Linked_list()
# LL.add_end(10)
# LL.add_end(20)
# LL.add_end(30)
# LL.add_end(20)
# LL.add_end(50)

# LL.print_LL()

# LL.remove_last_occurrence(20)

# print("\nAfter deletion:")
# LL.print_LL()


