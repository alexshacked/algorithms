from random import randint

class BinHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def insert(self, k):
        self.size = self.size + 1
        self.heap.append(k)
        self.percUp(self.size)

    def delMin(self):
        if self.size == 0:
            return None
        res = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap.pop(self.size)
        self.size = self.size - 1

        if self.size != 0:
            self.percDown(1)

        return res

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.size = len(alist)
        self.heap = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1

    def changeVal(self, i, val):
        'not standard heap API. required for the implementation of Dijkstra algorithm'
        self.heap[i] = val

        min_child = self.min(self.heap, i)
        father = i // 2

        if self.heap[father] > self.heap[i]:
            self.percUp(i)
        elif min_child and self.heap[min_child] < self.heap[i]:
            self.percDown(i)


    def percUp(self, i):
        while i // 2 > 0:
            up = i // 2
            if self.heap[i] < self.heap[up]:
                self.swap(self.heap, up, i)
            i = up

    def percDown(self, i):
        while i < self.size:
            smallest = self.min(self.heap, i)
            if smallest == None:
                break
            elif self.heap[ smallest ] < self.heap[i]:
                self.swap(self.heap, i, smallest)
                i = smallest
            else:
                break

    def swap(self, ls, one, two):
        tmp = ls[one]
        ls[one] = ls[two]
        ls[two] = tmp

    def min(self, ls, i):
        'between two children of i, will return the index of the one which has a smaller value'
        first = 2 * i
        sec = first + 1


        if sec > self.size and first <= self.size:
            res = first
        elif first > self.size:
            res = None
        else:
            if ls[first] <= ls[sec]:
                res = first
            else:
                res = sec

        return res

    ############################################### helpers ######################################################
    def show(self):
        'displays the heap internal data structure'
        i = 0;
        while i < len(self.heap):
            print '%d: %d' % (i, self.heap[i])
            i = i +1
        print '####################################################################################'

    def validate(self):
        'if not valid returns the index of not valid father. else returns 0'
        mid = self.size // 2
        i = 1; # we populate the heap starting from 1
        while i <= mid:
            father = self.heap[i]
            idx1 = i * 2
            idx2 = idx1 + 1
            child1 = self.heap[idx1] if idx1 <= self.size else None
            child2 = self.heap[idx2] if idx2 <= self.size else None
            if child1 and father > child1 or child2 and father > child2:
                return i
            i = i + 1

        return 0

    def num(self):
        'creates a random integer'
        n = randint(1, 1000)
        return n


if __name__ == '__main__':
    h = BinHeap()
    # input = [h.num() for _ in range(10)]
    # input = [92, 93, 207, 352, 286, 471, 771, 685, 782, 523]
    input = [523, 771, 207, 685, 286, 471, 93, 352, 782, 92]

    h.buildHeap(input)
    print('invalid node: %d' % h.validate())
    h.show()

    '''
    for i in input:
        h.insert(i)
    h.show()
    print('invalid node: %d' % h.validate())

    h.changeVal(10, 13)
    h.show()
    print('invalid node: %d' % h.validate())
    '''