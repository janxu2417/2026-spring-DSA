def main():
    def dfs(u):
        dp[u][1] = r[u]
        for v in children[u]:
            dfs(v)
            dp[u][0] += max(dp[v])
            dp[u][1] += dp[v][0]
        return

    n = int(input())
    r = [0]
    for i in range(n):
        r.append(int(input()))

    fa = [0] * (n + 1)
    children = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        fa[u] = v
        children[v].append(u)

    root = fa.index(0, 1)
    dp = [[0, 0] for _ in range(n + 1)]
    dfs(root)
    print(max(dp[root]))

if __name__ == '__main__':
    main()