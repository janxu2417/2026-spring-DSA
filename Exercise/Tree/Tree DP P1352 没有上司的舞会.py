import sys

sys.setrecursionlimit(10000)
def dfs(u, children, val, dp):
    dp[u][1] = val[u]
    for v in children[u]:
        dfs(v, children, val, dp)
        dp[u][1] += dp[v][0]
        dp[u][0] += max(dp[v])

def main():
    input = sys.stdin.readline
    n = int(input())
    r = [0]
    for i in range(n):
        r.append(int(input()))
    dp = [[0] * 2 for _ in range(n + 1)]
    children = [[] for _ in range(n + 1)]
    has_fa = [False] * (n + 1)
    has_fa[0] = True
    for _ in range(n - 1):
        l, k = map(int, input().split())
        has_fa[l] = True
        children[k].append(l)
    root = has_fa.index(False)

    dfs(root, children, r, dp)

    print(max(dp[root]))

if __name__ == '__main__':
    main()