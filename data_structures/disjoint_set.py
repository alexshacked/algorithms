
class DisjointSet:
    def __init__(self):
        self.forest = {}

    def makeSet(self, x):
        exist = self.forest.has_key(x)
        if not exist:
            self.forest[x] = {'parent': x, 'rank': 0}

    def find(self,x):
        exist = self.forest.has_key(x)
        if not exist:
            return None

        if self.forest[x]['parent'] != x:
            self.forest[x]['parent'] = self.find(self.forest[x]['parent'])

        return self.forest[x]['parent']

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)

        if xroot == yroot:
            return

        if self.forest[xroot]['rank'] < self.forest[yroot]['rank']:
            self.forest[xroot]['parent'] = yroot
        elif self.forest[xroot]['rank'] > self.forest[yroot]['rank']:
            self.forest[yroot]['parent'] = xroot
        else:
            self.forest[yroot]['parent'] = xroot
            self.forest[xroot]['rank'] = self.forest[xroot]['rank'] + 1



if __name__ == '__main__':
    set = DisjointSet()
    set.makeSet(1)
    set.makeSet(2)
    set.makeSet(3)
    set.makeSet(4)
    set.makeSet(5)
    set.makeSet(6)
    set.makeSet(7)
    set.makeSet(8)

    set.union(1, 2)
    set.union(2, 5)
    set.union(5, 6)
    set.union(6, 8)

    set.union(3, 4)

    print set.find(1) == set.find(8)
    print set.find(1) == set.find(7)


    print 'finished'
