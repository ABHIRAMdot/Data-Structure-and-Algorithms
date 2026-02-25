# class HashTable:
#     def __init__(self):
#         self.MAX  = 10
#         self.arr = [[] for i in range(self.MAX)]
#         self.n = 0

#     def get_hash(self, key):
#         h = 0
#         for char in key:
#             h += ord(char)
#         return h % self.MAX
    
#     def add(self, key, val):
#         h = self.get_hash(key)
#         found = False
#         for idx, element in enumerate(self.arr[h]):
#             if len(element) == 2 and element[0] == key:
#                 self.arr[h][idx] = (key, val)
#                 found = True
#                 break
#         if not found:
#             self.arr[h].append((key, val))
#             self.n += 1

#     def get(self, key):         # arr[h] = [ (key, value), (key, value)]
#         h = self.get_hash(key)
#         for element in self.arr[h]:
#             if element[0] == key:
#                 return element[1]
    
#     def delete(self, key):
#         h = self.get_hash(key)
#         for idx, element in enumerate(self.arr[h]):
#             if len(element) == 2 and element[0] == key:
#                 del self.arr[h][idx]
#                 self.n -= 1
#                 break





# t = HashTable()
# t.add('march 6', 130)
# t.add('dec 2', 20)
# t.add('dec 17', 27)
# t.add('march 17', 450)
# t.add('march 6', 500)

# t.delete('march 17')
# # t.delete('march 1')                               
# print(t.arr)

# print(t.get('march 6')) 

# # print(t.get_hash('march 17'))










class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
        self.n = 0

    def get_hah(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    # def get_hash(self, key):
    #     return key % self.MAX
    
    def __getitem__(self, key):
        h = self.get_hah(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]


    def __setitem__(self, key, val):
        h = self.get_hah(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
                break
        if not found:
            self.arr[h].append((key,val))
            self.n += 1



    def __delitem__(self, key):
        h = self.get_hah(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]
                self.n -= 1
                break
    #Load factor
    def load_factor(self):
        return self.n / self.MAX



t = HashTable()
t['march 6'] =  2000
t['march 4'] = 3000
t['dec 2'] = 4000
t['march 17'] = 5500

# del t['dec 2']

print(t.arr)
print(t['march 6'])
print(t.load_factor())

# print(t.get_hah("march 17"))






