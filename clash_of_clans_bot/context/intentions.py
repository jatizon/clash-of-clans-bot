

class Intentions():
    def __init__(self):
        self.intentions = set()

    def set(self, intention):
        self.intentions.add(intention)

    def clear(self, intention):
        self.intentions.discard(intention)

    def has(self, intention):
        return intention in self.intentions
        