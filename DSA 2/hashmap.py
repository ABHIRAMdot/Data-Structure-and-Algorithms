# def get_hash(key):
#     h = 0
#     for char in key:
#         h += ord(char)
#     return h % 100

# # print(get_hash("march 6"))



class HashTable:
    def __init__(self):
        self.MAX  = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def add(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def get(self, key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def delete(self, key):
        h = self.get_hash(key)
        self.arr[h] = None
    





t = HashTable()
t.add('march 6', 130)
t.add('march 1', 20)
t.add('dec 17', 27)
t.add('march 17', 450)

# t.delete('march 1')                               
print(t.arr)

print(t.get('march 6'))

# print(t.get_hash('march 17'))