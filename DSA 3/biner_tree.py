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

def inorder(root):
    if root is None:
        return 
    
    inorder(root.left)
    print(root.data)
    inorder(root.right)


def postorder(root):
    if root is None:
        return
    
    postorder(root.left)
    postorder(root.right)
    print(root.data)



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




