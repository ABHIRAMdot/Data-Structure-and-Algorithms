class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]

        node.end = True

    # helper DFS, here path is the prefix 
    def dfs(self, node, path, result):
        if node.end:
            result.append(path)

        for i in node.children:
            self.dfs(node.children[i], path + i, result)
    
    def autocomplete(self, prefix):
        node = self.root

        for i in prefix:
            if i not in node.children:
                return []    #no suggessions
            node = node.children[i]

        result = []
        self.dfs(node, prefix, result)

        return result



# tr = Trie()
# tr.insert("app")
# tr.insert("apple")
# tr.insert("ape")
# tr.insert("bat")
# tr.insert("ball")

# print(tr.autocomplete("ap"))


# print(tr.autocomplete("app"))   # ['app', 'apple']
# print(tr.autocomplete("ba"))    # ['bat', 'ball']
# print(tr.autocomplete("z"))     # []

#-------------------------------------------------------

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()

            node = node.children[i]

        node.end = True
    
    def dfs(self, node, path, result):
        if node.end:
            result.append(path)

        for i in node.children:
            self.dfs(node.children[i], path + i, result)

    def autocomplete(self, prefix):
        node = self.root

        for i in prefix:
            if i not in node.children:
                return []
            node = node.children[i]

        result = []
        self.dfs(node, prefix, result)
        return result


# tr = Trie()
# tr.insert("app")
# tr.insert("apple")
# tr.insert("ape")
# tr.insert("bat")
# tr.insert("ball")

# print(tr.autocomplete("ap"))

#---------------------------------

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]

        node.end = True
    
    def dfs(self, node, path, result):
        if node.end:
            result.append(path)
        
        for i in node.children:
            self.dfs(node.children[i], path + i, result)

    def autocomplete(self, prefix):
        node = self.root

        for i in prefix:
            if i not in node.children:
                return []
            node = node.children[i]
        
        result = []
        self.dfs(node, prefix, result)
        return result

tr = Trie()

tr.insert("app")
tr.insert("apple")
tr.insert("ape")
tr.insert("bat")
tr.insert("ball")

print(tr.autocomplete("b"))
