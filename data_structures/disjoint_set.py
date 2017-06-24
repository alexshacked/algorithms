
class DisjointSet:
    def __init__(self):
        self.tree = {}

    def makeSet(self, x):
        exist = self.tree.has_key(x)
        if not exist:
            self.tree[x] = {'parent': x, 'rank': 0}

    def find(self,x):
        exist = self.tree.has_key(x)
        if not exist:
            return None

        if self.tree[x]['parent'] != x:
            self.tree[x]['parent'] = self.find(self.tree[x]['parent'])

        return self.tree[x]['parent']

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)

        if xroot == yroot:
            return

        if self.tree[xroot]['rank'] < self.tree[yroot]['rank']:
            self.tree[xroot]['parent'] = yroot
        elif self.tree[xroot]['rank'] > self.tree[yroot]['rank']:
            self.tree[yroot]['parent'] = xroot
        else:
            self.tree[yroot]['parent'] = xroot
            self.tree[xroot]['rank'] = self.tree[xroot]['rank'] + 1



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
