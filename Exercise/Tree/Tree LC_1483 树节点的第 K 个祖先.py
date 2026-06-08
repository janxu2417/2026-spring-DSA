from typing import List

class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.n = n
        self.fa = [parent]
        i = 1
        while (1 << i) < n:
            last = self.fa[-1]
            tmp = [-1]
            for j in range(1, n):
                if last[j] == -1:
                    tmp.append(-1)
                else:
                    tmp.append(last[last[j]])
            self.fa.append(tmp)
            i += 1

    def getKthAncestor(self, node: int, k: int) -> int:
        if k > self.n - 1:
            return -1
        i = 0
        while k and node >= 0:
            if k & 1:
                node = self.fa[i][node]
            k >>= 1
            i += 1
        return node

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
