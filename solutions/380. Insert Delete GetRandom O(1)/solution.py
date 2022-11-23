import random


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
class RandomizedSet:
    def __init__(self):
        self.values = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        not_found = True if val not in self.indices else False
        if not_found:
            self.indices[val] = len(self.values)
            self.values.append(val)
        return not_found

    def remove(self, val: int) -> bool:
        found = True if val in self.indices else False
        if found:
            if self.values[-1] != val:
                last_val = self.values[-1]
                idx_val = self.indices[val]
                self.indices[last_val], self.indices[val] = self.indices[val], self.indices[last_val]
                self.values[idx_val], self.values[-1] = self.values[-1], self.values[idx_val]
            self.indices.pop(val)
            self.values.pop()
        return found

    def getRandom(self) -> int:
        idx = random.randint(0, len(self.values) - 1)
        return self.values[idx]
