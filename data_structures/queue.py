class Queue:
    def __init__(self):
        self.q = []

    def enque(self, a):
        self.q.append(a)

    def deque(self):
        r = self.q.pop(0)
        return r

    def empty(self):
        return len(self.q) == 0

    def size(self):
        return len(self.q)

    def show(self):
        for i in self.q: print i,
