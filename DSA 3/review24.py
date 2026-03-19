class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

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

    


b =  BinaryTree(10)
b.left = BinaryTree(20)
b.right = BinaryTree(30)
b.left.left = BinaryTree(50)



# print(b.key, '--> root')
# print(b.left.key, '--> left')
# print(b.right.key, '--> right')

# print(b.height())


#-------------------------------------


# class MaxHeap:
#     def __init__(self):
#         self.heap = []

#     def insert(self, data):
#         self.heap.append(data)
#         self.heapify_up(len(self.heap) -1)

#     def heapify_up(self, index):
#         parent = (index - 1)// 2

#         if index > 0 and self.heap[index] > self.heap[parent]:
#             self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
#             self.heapify_up(parent)

#     def display(self):
#         for i in self.heap:
#             print(i, end="-->")
    
# m = MaxHeap()
# m.insert(10)
# m.insert(20)
# m.insert(5)
# m.insert(30)

# m.display()


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()



    for i in graph[node]:
        if i not in visited:
            print(i)
            visited.add(i)            
            dfs(graph, i, visited)

dfs(graph, 'A')