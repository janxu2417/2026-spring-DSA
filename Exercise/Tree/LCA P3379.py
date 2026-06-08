from typing import List
import sys

class TreeAncestor:

    def __init__(self, n: int, root: int, edge: List[List[int]]) -> None:
        
        def build_tree():
            st = [(root, 0)]
            while st:
                node, pre = st.pop()
                self.depth[node] = self.depth[pre] + 1
                parent[node] = pre
                for child in edge[node]:
                    if child != pre:
                        st.append((child, node))

        parent = [0] * (n + 1)
        self.depth = [0] * (n + 1)
        self.n = n
        self.fa = [parent]
        build_tree()
        i = 1
        while (1 << i) < n:
            last = self.fa[-1]
            tmp = [0]
            for j in range(1, n + 1):
                if last[j] == 0:
                    tmp.append(0)
                else:
                    tmp.append(last[last[j]])
            self.fa.append(tmp)
            i += 1

    def get_lca(self, x: int, y: int) -> int:
        if self.depth[x] < self.depth[y]:
            x, y = y, x
        d = self.depth[x] - self.depth[y]

        i = 0
        while d > 0:
            if d & 1:
                x = self.fa[i][x]
            d >>= 1
            i += 1
        if x == y:
            return x
        i = len(self.fa) - 1
        while i >= 0:
            if self.fa[i][x] != self.fa[i][y]:
                x = self.fa[i][x]
                y = self.fa[i][y]
            i -= 1
        return self.fa[0][x]

def main():
    it = iter(sys.stdin.read().split())
    n = int(next(it))
    m = int(next(it))
    root = int(next(it))
    edge = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        x = int(next(it))
        y = int(next(it))
        edge[x].append(y)
        edge[y].append(x)
    tree = TreeAncestor(n, root, edge)
    for _ in range(m):
        x = int(next(it))
        y = int(next(it))
        sys.stdout.write(str(tree.get_lca(x, y)) + '\n')

if __name__ == '__main__':
    main()
    
