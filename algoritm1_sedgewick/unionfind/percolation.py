from unionfind import UF

class Percolation:
    def __init__(self, N):
        self._sites = [ [False  for i in range(N)] for i in range(N)]
        self.uf = UF(N*N+2)

        # root of lower layer -> node idx N*N
        for i in range(N):
            idx = self._2dim_to_1dim(N-1, i)
            self.uf.union(N*N, idx)
        # root of upper layer > node idx N*N+1
        for i in range(N):
            idx = self._2dim_to_1dim(0, i)
            self.uf.union(N*N+1, idx)


    def open(self, row, col): # row 1 - N, col: 1 - N
        row -= 1
        col -= 1
        self._sites[row][col] = True
        idx = self._2dim_to_1dim(row, col)

        if row > 0 and self._sites[row-1][col] == True: #up
            up = self._2dim_to_1dim(row - 1, col)
            self.uf.union(idx, up)
        if row < (self._width() - 1) and self._sites[row +1][col] == True: #down
            down = self._2dim_to_1dim(row + 1, col)
            self.uf.union(idx, down)
        if col > 0 and self._sites[row][col-1] == True: #behind
            behind = self._2dim_to_1dim(row, col - 1)
            self.uf.union(idx, behind)
        if col < (self._width() - 1) and self._sites[row][col + 1] == True: #in front
            front = self._2dim_to_1dim(row, col + 1)
            self.uf.union(idx, front)

    def isOpen(self, row, col):
        row -= 1
        col -= 1
        return self._sites[row][col] == True

    def isFull(self, row, col):
        row -= 1
        col -= 1
        if not self._sites[row][col]:
            return False
        w = self._width()
        idx = self._2dim_to_1dim(row, col)
        return self.uf.connected(idx, w*w + 1)

    def numberOfOpenSites(self):
        open = [ 1  for i in self._sites for j in i if j == True]
        return sum(open)

    def percolates(self):
        w = self._width()
        return self.uf.connected(w*w, w*w+1)

    def _width(self):
        return len(self._sites[0])

    def _2dim_to_1dim(self, i, j):
        sz = self._width()
        return i*sz + j

    def _1dim_to_2dim(self, idx):
        sz = self._width()
        i = idx // sz
        j = idx % sz
        return (i, j)

    def _show_sites(self):
        sz = len(self._sites[0])
        header_piece = "%-5d"
        cols_header_template = header_piece * sz

        cols_header = ' ' * 5 + cols_header_template % tuple(range(1, sz+1))
        print(cols_header)

        val_template = "%-5s"
        for pair in enumerate(self._sites):
            row_header = header_piece % (pair[0] +1)

            pieces = []
            for b in pair[1]:
                if b:
                    one = '\033[1m' + val_template % 't' + '\033[0m'
                else:
                    one = val_template % 'F'
                pieces.append(one)
            tup = tuple(pieces)

            val_line = (val_template * sz) % tup
            val_line = row_header + val_line
            print(val_line)



if __name__ == '__main__':
    per = Percolation(5)
    per._show_sites()
    per.open(2,4)
    per.open(3,4)
    per._show_sites()
    print(per.numberOfOpenSites())
