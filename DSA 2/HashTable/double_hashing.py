class HashMap:
    def __init__(self):
        self.size = 11   # prime number
        self.table = [None] * self.size
        self.DELETED = object()

    # Primary hash
    def h1(self, key):
        return key % self.size

    # Secondary hash (step size)
    def h2(self, key):
        return 1 + (key % (self.size - 1))

    def put(self, key, value):
        index1 = self.h1(key)
        step = self.h2(key)

        for i in range(self.size):
            index = (index1 + i * step) % self.size

            if self.table[index] is None or self.table[index] is self.DELETED:
                self.table[index] = (key, value)
                return

            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return

        print("HashMap is full")

    def get(self, key):
        index1 = self.h1(key)
        step = self.h2(key)

        for i in range(self.size):
            index = (index1 + i * step) % self.size

            if self.table[index] is None:
                return None

            if self.table[index] is self.DELETED:
                continue

            if self.table[index][0] == key:
                return self.table[index][1]

        return None

    def delete(self, key):
        index1 = self.h1(key)
        step = self.h2(key)

        for i in range(self.size):
            index = (index1 + i * step) % self.size

            if self.table[index] is None:
                return

            if self.table[index] is self.DELETED:
                continue

            if self.table[index][0] == key:
                self.table[index] = self.DELETED
                return

    def display(self):
        result = []
        for item in self.table:
            if item is self.DELETED:
                result.append("D")
            else:
                result.append(item)
        print(result)
