class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()


    def insert(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()

            node = node.children[ch]

        node.end = True

    def search(self, word):
        node = self.root

        for i in word:
            if i not in node.children:
                return False
            node = node.children[i]

        return node.end 


    def prifix_startsWith(self, prefix):
        node = self.root

        for i in prefix:
            if i not in node.children:
                return False
            node = node.children[i]

        return True
    

# tr =Trie()

# tr.insert("app")
# tr.insert("apple")

# print(tr.search("app"))
# print(tr.search("apple"))
# print(tr.search('ap'))
# print(tr.prifix_startsWith("ap"))
# print(tr.prifix_startsWith("banana"))


#--------------------------------------------

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.count = 0 # for getting count (number of words passing through)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
            node.count += 1   #increment at each step

        node.end  = True

    def search(self, word):
        node = self.root

        for i in word:
            if i not in node.children:
                return False
            node = node.children[i]

        return node.end
    
    def startsWith(self, prefix):
        node = self.root

        for i in prefix:
            if i not in node.children:
                return False
            node = node.children[i]

        return True

    def countWordsStartingWith(self, prefix):
        node = self.root

        for i in prefix:
            if i not in node.children:
                return 0
            node = node.children[i]

        return node.count

tr =Trie()

tr.insert("app")
tr.insert("apple")

print(tr.search(" "))
print(tr.search("apple"))
print(tr.search('ap'))
print(tr.startsWith("ap"))
print(tr.startsWith("banana"))
print(tr.countWordsStartingWith('app'))

