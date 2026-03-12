class NodeAVL:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def getHeight(node):
    if not node:
        return 0    
    return node.height

def getBalance(node):
    if not node:
        return 0
    return getHeight(node.left) - getHeight(node.right)

def rightRotate(z):
    y = z.left
    T3 = y.right

    y.right = z
    z.left = T3

    # updata heights

    z.height = 1 + max(getHeight(z.left), getHeight(z.right))
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))

    return y


def insert(root, key):
    if not root:
        return NodeAVL(key)
        
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root
    # update height
    root.height = 1 + max(getHeight(root.left), getHeight(root.right))
    # check balance
    balance = getBalance(root)

    # LL case
    if balance > 1 and key < root.left.key:
        return rightRotate(root)
    
    return root


root = None

root = insert(root,30)
root = insert(root, 20)
root = insert(root, 10)
