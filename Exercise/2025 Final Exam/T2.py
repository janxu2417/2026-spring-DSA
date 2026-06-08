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
    fa = list(range(n + 1))
    rank = [0] * (n + 1)

    count = 0
    ans = 0
    for w, u, v in adj:
        if union(u, v):
            ans += w
            count += 1
        if count == n - 1:
            break

    if count == n - 1:
        print(ans)
        return True
    return False

def main():
    n, m = map(int, input().split())
    adj = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj.append((w, u, v))
    if not kruskal(adj, n):
        print("orz")

if __name__ == '__main__':
    main()