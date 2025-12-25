


class Blackboard:
    def __init__(self):
        self.memory = {}

    def set(self, key, value):
        self.memory[key] = value

    def get(self, key, default=None):
        return self.memory.get(key, default)

    def has(self, key):
        return key in self.memory

    def remove(self, key):
        self.memory.pop(key, None)

    def clear(self):
        self.memory.clear()

    def add(self, key, delta=1):
        self.set(key, self.get(key) + delta)
        return self.get(key)
