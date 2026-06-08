from typing import List

class UnionFind:
    def __init__(self, n):
        self.fa = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        fa = self.fa
        while fa[x] != x:
            fa[x] = fa[fa[x]]
            x = fa[x]
        return x

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return True
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.fa[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        return False

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:

        if len(edges) < n - 1:
            return -1

        uf = UnionFind(n)
        edge_cnt = 0
        mins = 10 ** 6
        for x, y, w, must in edges:
            if must:
                if uf.union(x, y):
                    return -1
                edge_cnt += 1
                mins = min(mins, w)
        if edge_cnt == n - 1:
            return mins

        edges.sort(key=lambda x: -x[2])
        a = []
        for x, y, w, must in edges:
            if not must and not uf.union(x, y):
                edge_cnt += 1
                a.append(w)
                if edge_cnt == n - 1:
                    break
        if edge_cnt < n - 1:
            return -1
        mins = min(mins, a[-1] << 1)
        if k < len(a):
            mins = min(mins, a[-1-k])
        return mins


