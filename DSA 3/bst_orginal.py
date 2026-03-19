from collections import deque
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

    
    def levelorder(self):
        queue = deque()
        queue.append(self)

        while queue:
            node = queue.popleft()
            print(node.key, end=" ")

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)


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
            if self.left is None and self.right is None:
                return None
            
            if self.left is None:
                return self.right
            
            if self.right is None:
                return self.left
            
            node = self.right.find_min()
            self.key = node.key
            self.right = self.right.deleteBST(node.key)

        return self
    

    def second_largest(self):
        if self.right:
            if self.right.right is None and self.right.left is None:
                return self.key
            
            return self.right.second_largest()
        
        return self.left.find_max()
    
    def find_max(self):
        if self.right is None:
           return self.key

        return self.right.find_max()
    

    def closest_value(self, target, closest=None):
        if closest is None:
            closest = self.key

        if abs(target - self.key) < abs(target - closest):
            closest = self.key

        if target < self.key and self.left:
            return self.left.closest_value(target, closest)
        
        elif target > self.key and self.right:
            return self.right.closest_value(target, closest)
        return closest    
    
    def height(self):
        
        left_height = -1
        right_height = -1

        if self.key is None:
            return 0

        if self.left:
            left_height = self.left.height()
        if self.right:
            right_height = self.right.height()

        return max(left_height, right_height) + 1
    
    def depth_of_node(self, val, d=0):
        if self.key == val:
            return d 
        
        if val < self.key and self.left:
            return self.left.depth_of_node(val, d+1)
        if val > self.key and self.right:
            return self.left.depth_of_node(val, d+1)
        
        return -1
    
    def count_of_nodes(self):
        left_count = 0
        right_count = 0

        if self.key is None:
            return 0

        if self.left:
            left_count = self.left.count_of_nodes()
        if self.right:
            right_count = self.right.count_of_nodes()
        
        return left_count + right_count + 1
    
    def sum_of_nodes(self):
        left_total = 0
        right_total = 0

        if self.key is None:
            return 0
        
        if self.left:
            left_total = self.left.sum_of_nodes()

        if self.right:
            right_total = self.right.sum_of_nodes()

        return left_total + right_total + self.key
    
    
    


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

# root.levelorder()

# print(root.depth_of_node(10))

print(root.height())

print(root.count_of_nodes())

print(root.sum_of_nodes())
# root.postorder()
# print()

# root.deleteBST(10)
# print()

# root.inorder()

#--------------------------------------------------------------

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

#-----------------------------------------------------------------------

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

#-----------------------------------------------------------------------

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

#-----------------------------------------------------------------------

def find_smallest(root):
    if root.left is None:
        return root.key
    return find_smallest(root.left)

# print(find_smallest(root))

#-----------------------------------------------------------------------
