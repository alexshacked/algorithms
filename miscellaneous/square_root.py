
class SQ:
    def __init__(self):
        pass

    def seq(self, end):
        n = 1
        r0 = 0
        r1 = 1

        while r1 < end:
            delta1 = r1 - r0
            delta2 = delta1 + 2
            print('%5d   %5d   %5d' % (n, r1, delta2))
            r0 = r1
            r1 = r1 + delta2
            n  += 1

        if r1 == end:
            print('%5d   %5d   %5d' % (n, r1, r1 - r0))
            print("%d has a root" % end)
        else:
            print("%d does not have a root" % end)

if __name__ == '__main__':
    sq = SQ()
    sq.seq(1000)


