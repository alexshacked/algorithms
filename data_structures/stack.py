
class Stack:
    def __init__(self):
        self.items = []

    def push (self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)
