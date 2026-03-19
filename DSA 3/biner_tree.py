# pre order
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder(root):
    if root is None:
        return 
    
    print(root.data)
    preorder(root.left)
    preorder(root.right)

#--------------------------

def inorder(root):
    if root is None:
        return 
    
    inorder(root.left)
    print(root.data)
    inorder(root.right)

#-----------------------------

def postorder(root):
    if root is None:
        return
    
    postorder(root.left)
    postorder(root.right)
    print(root.data)

#-----------------------------------

from collections import deque

def level_order(root):
    if root is None:
        return
    
    q = deque([root])

    while q:
        node = q.popleft()
        print(node.data)

        if node.left:
            q.append(node.left)

        if node.right:
            q.append(node.right)

#------------------------------------
#height of a Binary tree

def height(root):
    if root is None:
        return -1
    
    left_h = height(root.left)
    right_h = height(root.right)

    return 1 + max(left_h, right_h)

#------------------------------------

# count of leaf nodes

def count_leaf(root):
    if root is None:
        return 0
    
    if root.left is None and root.right is None:
        return 1
    
    return count_leaf(root.left) + count_leaf(root.right)


#-----------------------------------------------------------
#count internal nodes
def count_internal(root):
    if root is None or (root.left is None and root.right is None):
        return 0
    
    return 1 + count_internal(root.left) + count_internal(root.right)

#-----------------------------------------------------------------------

# check  node has either 0 or 2 children to check if Tree is full

def is_full(root):
    if root is None:
        return True
    
    if root.left is None and root.right is None:
        return None
    
    if root.left and root.right:
        return is_full(root.left) and is_full(root.right)
    
    return False
#---------------------------------------------------------------------
# Check the tree is perfect
    # 1️⃣ Count nodes
    # 2️⃣ Calculate height
    # 3️⃣ Apply formula


def height(root):
    if root is None:
        return -1
    
    left_h = height(root.left)
    right_h = height(root.right)

    return 1 + max(left_h, right_h)

# def count_internal(root):
#     if root is None:
#         return 0
    
#     return 1 + count_internal(root.left) + count_internal(root.right)


def is_perfect(root):
    h = height(root) + 1
    nodes = count_internal(root)

    return nodes == (2 ** h -1)

#---------------------------------------

# Check if the Tree is balanced

def is_balance(root):
    if root is None:
        return True
    
    left_h = height(root.left)
    right_h = height(root.right)

    if abs(left_h - right_h) >1:
        return False
    
    return is_balance(root.left) and is_balance(root.right)



root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(5)
root.right.right = Node(6)
root.right.right.right = Node(7)


# postorder(root)

# print(count_leaf(root))
# print(count_internal(root))















