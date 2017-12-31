# union find

class UF:
    def __init__(self, N):
        self._frst = [i for i in range(N)]
        self._wght = [1] * N

    def union(self, p, q):
        rp = self._root(p)
        rq = self._root(q)

        if rp == rq:
            return

        if self._wght[rp] >= self._wght[rq]:
            self._frst[rq] = rp
            self._wght[rp] += self._wght[rq]
        else:
            self._frst[rp] = rq
            self._wght[rq] += self._wght[rp]

    def connected(self, p, q):
        rp = self._root(p)
        rq = self._root(q)
        return rp == rq


    def find(self, p): # returns root
        return self._root(p)

    def count(self):
        return sum([1 for i in range(len(self._frst)) if \
                   self._frst[i] == i ])

    def _root(self, p):
        while p != self._frst[p]:
            self._frst[p] = self._frst[self._frst[p]] # flattening of tree
            p = self._frst[p]
        return p

    def _dbg_frst(self):
        for t in enumerate(self._frst):
            print("%d:  %d" % (t[0], t[1]))

    def _dbg_wght(self):
        for t in enumerate(self._wght):
            print("%d:  %d" % (t[0], t[1]))

if __name__ == '__main__':
    def show_connected(uf, a, b):
        print('connnected %d - %d: %d' % (a, b, uf.connected(a, b)))

    def show_components(uf):
        print("components: %d" % uf.count())

    uf  = UF(10)
    uf.union(4, 3)
    uf.union(4, 8)
    uf.union(4, 9)
    uf.union(6, 0)
    uf.union(6, 5)
    uf.union(2, 1)
    uf.union(2, 7)
    show_connected(uf, 3, 0)
    show_components(uf)
    uf.union(5, 1)
    uf.union(3, 0)
    uf._dbg_frst()
    uf._dbg_wght()
    show_connected(uf, 3, 0)
    show_components(uf)





