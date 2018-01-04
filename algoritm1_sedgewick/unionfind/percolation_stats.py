# percolation_stats.py - evaluates percolation algorithm

import percolation
import math
import random
import sys

'''
1. Attention! The Percolation API accepts row, columnd indexes starting from 1, not 0.
'''

class PercolationStats:
    def __init__(self, N, trials):
        self.percs = []
        self.trials = trials
        for i in range(trials):
            one_percolation_rate = self._one_trial(N)
            self.percs.append(one_percolation_rate)
            print('%-10d%-17.16f' % (i+1,one_percolation_rate))

        self._mn = None
        self._std = None
        self.conf_low = None
        self.conf_high = None

    def mean(self):
        if self._mn != None:
            return self._mn
        self._mn = sum(self.percs)/self.trials
        return self._mn

    def stddev(self):
        if self._std != None:
            return self._std
        man = self.mean()
        deltas = [ (p - man)**2 for p in self.percs]
        avg_deltas = sum(deltas)/(len(self.percs) - 1)
        self._std = math.sqrt(avg_deltas)
        return self._std

    def confidenceLow(self):
        if self.conf_low != None:
            return self._conf_low
        self._conf_low = self.mean() - 1.96 * self.stddev() / math.sqrt(len(self.percs))
        return self._conf_low

    def confidenceHigh(self):
        if self.conf_high != None:
            return self.conf_high
        self.conf_high = self.mean() + 1.96 * self.stddev() / math.sqrt(len(self.percs))
        return self.conf_high

    def _one_trial(self, N):
        sites = N * N
        pr = percolation.Percolation(N)
        while not pr.percolates():
            rint = random.randint(1, sys.maxint)
            rix = rint % sites
            row, col = pr._1dim_to_2dim(rix)
            pr.open(row +1, col+1)
        # pr._show_sites()

        open_sites = pr.numberOfOpenSites()
        per_ratio =  open_sites * 1.0 / sites
        return per_ratio

if __name__ == '__main__':
    N = 200
    trials = 100
    ps = PercolationStats(N, trials)
    print('%-25s= %-17.16f' % ('mean', ps.mean()))
    print('%-25s= %-18.17f' % ('stddev', ps.stddev()))
    print('%-25s= [%-17.16f, %-17.16f]' % ('95% confidence interval', ps.confidenceLow(), ps.confidenceHigh()))