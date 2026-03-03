class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None] * self.MAX
        self.DELETED = object()

    # for string hashing
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    # for integer hashing
    # def get_hash(self, key):
    #     return key % self.MAX
    
    def add(self, key, val):
        h = self.get_hash(key)

        for i in range(self.MAX):
            new_index = (h + i) % self.MAX

            if self.arr[new_index] is None or self.arr[new_index] is self.DELETED:
                self.arr[new_index] = (key, val)
                return 
            
            if self.arr[new_index][0] == key:
                self.arr[new_index] = (key, val)
                return 
            
        print("Hash Table is full")

    def get(self, key):
        h = self.get_hash(key)

        for i in range(self.MAX):
            new_index = (h + i) % self.MAX

            if self.arr[new_index] is None:
                return
            
            if self.arr[new_index] is self.DELETED:
                continue
            
            if self.arr[new_index][0] == key:
                return self.arr[new_index][1]
        
        return None
    

    def delete(self, key):
        h = self.get_hash(key)

        for  i in range(self.MAX):
            new_index = (h + i) % self.MAX

            if self.arr[new_index] is None:
                return 
            
            if self.arr[new_index] is self.DELETED:
                continue    
            
            if self.arr[new_index][0] == key:
                self.arr[new_index] = self.DELETED
                return 
    
    def display(self):
        result = []
        for i in self.arr:
            if i is self.DELETED:
                result.append('D')
            else:
                result.append(i)
        print(result)

t = HashTable()

t.add('march 6', 32)
t.add('march 7', 99)    
t.add('dec 2', 44)
t.add('march 17', 55)
t.add('march 1', 35)
t.add('march 4', 65)
t.add('march 5', 55)
t.add('march 66', 775)
t.delete('march 17')

t.display()
print(t.get('march 1'))

