class BST:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insertBST(self, data):
        if self.key is None:
            self.key = data
            return
        
        if self.key  == data:
            return
        
        if data < self.key:
            if self.left:
                self.left.insertBST(data)
            else:
                self.left = BST(data)
        
        else:
            if self.right:
                self.right.insertBST(data)
            else:
                self.right = BST(data)

        
    def searchBST(self, data):
        if self.key == data:
            print("node is found")
            return True
        
        if data < self.key:
            if self.left:
                return self.left.searchBST(data)
            else:
                print("Node not found")
                return False
        
        else:
            if self.right:
                return self.right.searchBST(data)
            else:
                print("node not found")
                return False
            

    def preorder(self):
        print(self.key, end=" ")
        
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

        
    def inorder(self):
        if self.left:
            self.left.inorder()

        print(self.key, end=" ")

        if self.right:
            self.right.inorder()

        
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()

        print(self.key, end=" ")


    def find_min(self):
        current = self
        while current.left:
            current = current.left
        return current

    def deleteBST(self, data):
        if data < self.key:
            if self.left:
                self.left = self.left.deleteBST(data)
            else:
                print("node not found")

        elif data > self.key:
            if self.right:
                self.right = self.right.deleteBST(data)
            else:
                print("node not found")

        else:
            if self.right is None and self.right is None:
                return None
            
            if self.left is None:
                return self.right
            
            if self.right is None:
                return self.left
            
            node = self.right.find_min()
            self.key = node.key
            self.right = self.right.deleteBST(node.key)

        return self
    


root = BST(21)
val = [10,30,5,3,3,12,25,100,3,7]

for i in val:
    root.insertBST(i)

# root.searchBST(50)
# print()
# root.preorder()
# print()
root.inorder()
print()
# root.postorder()
# print()

# root.deleteBST(10)
# print()

# root.inorder()


def is_bst(node, min_val=float('-inf'), max_val=float('inf')):
    if node is None:
        return True
    
    if not(min_val < node.key < max_val):
        return False
    
    return (
        is_bst(node.left, min_val, node.key) and is_bst(node.right, node.key, max_val)
    )

# print()
# print(is_bst(root))


def identical(t1, t2):
    if t1 is None and t2 is None:
        return True
    
    if t1 is None or t2 is None:
        return False
    
    if t1.key != t2.key:
        return False
    
    return (
        identical(t1.left, t2.left) and 
        identical(t1.right, t2.right)
    )


# tree1 = BST(50)
# tree1.insertBST(30)
# tree1.insertBST(70)

# tree2 = BST(50)
# tree2.insertBST(70)
# tree2.insertBST(75)

# print(identical(tree1, tree2))

def kth_smallest(root, k):
    stack = []

    def inorder_small(node):
        if node is None:
            return

        # inorder_small(node.right) #if kth largest
        inorder_small(node.left)
        stack.append(node.key)
        inorder_small(node.right)
        # inorder_small(node.left)  #if kth largest

    inorder_small(root)

    return stack[k-1]

# print(kth_smallest(root,3))

def find_smallest(root):
    if root.left is None:
        return root.key
    return find_smallest(root.left)

print(find_smallest(root))