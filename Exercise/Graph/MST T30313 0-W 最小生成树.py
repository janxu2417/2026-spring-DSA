import sys
from collections import deque

def to_point(adj_set, n):
    un_vis = set(range(1, n))
    comp = [-1] * n

    def bfs(u):
        nonlocal cnt
        q = deque()
        q.append(u)
        comp[u] = cnt
        un_vis.remove(u)
        while q:
            v = q.popleft()
            for x in list(un_vis):
                if x not in adj_set[v]:
                    q.append(x)
                    un_vis.remove(x)
                    comp[x] = cnt

    cnt = 0
    for i in range(1, n):
        if comp[i] == -1:
            bfs(i)
            cnt += 1
    return comp, cnt

def kruskal(adj, n):

    def find(x):
        while fa[x] != x:
            fa[x] = fa[fa[x]]
            x = fa[x]
        return x

    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return False
        if rank[x] < rank[y]:
            x, y = y, x
        fa[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1
        return True

    adj.sort()
    fa = list(range(n))
    rank = [0] * n

    count = 0
    ans = 0
    for w, u, v in adj:
        if union(u, v):
            ans += w
            count += 1
        if count == n - 1:
            break
    return ans


def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj_set = [set() for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        a, b, w = map(int, input().split())
        adj_set[a].add(b)
        adj_set[b].add(a)
        edges.append((a, b, w))
    comp, cnt = to_point(adj_set, n + 1)
    comp_adj = []
    for u, v, w in edges:
        u = comp[u]
        v = comp[v]
        if u != v:
            comp_adj.append((w, u, v))

    print(kruskal(comp_adj, cnt))

if __name__ == '__main__':
    main()
