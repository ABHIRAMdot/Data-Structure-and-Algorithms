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
# root.inorder()
# print()
# root.postorder()
# print()

root.deleteBST(10)
print()

root.inorder()