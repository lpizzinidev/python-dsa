"""
UnionFind class.

Implements a UnionFind data structure optimized with
path compression and union by rank.
"""
class UnionFind:
    def __init__(self, size):
        self.size = size
        self.root = [i for i in range(self.size)]
        self.rank = [1] * self.size

    def find(self, p):
        if p == self.root[p]: return p
        self.root[p] = self.find(self.root[p])
        return self.root[p]

    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q: return
        if self.rank[root_p] > self.rank[root_q]:
            self.root[root_q] = root_p
        elif self.rank[root_p] < self.rank[root_q]:
            self.root[root_p] = root_q
        else:
            self.root[root_q] = root_p
            self.rank[root_p] += 1
        self.size -= 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def components(self):
        return self.size
