import sys

sys.setrecursionlimit(2000)
def tarjan_scc(graph):
    n = len(graph)
    timer = 0
    dfn = [-1] * n
    low = [-1] * n
    on_stack = [False] * n
    stack = []
    sccs = []

    def dfs(u):
        nonlocal timer
        dfn[u] = low[u] = timer
        timer += 1
        on_stack[u] = True
        stack.append(u)

        v = graph[u]
        if dfn[v] == -1:
            dfs(v)
            low[u] = min(low[u], low[v])
        elif on_stack[v]:
            low[u] = min(low[u], dfn[v])

        if dfn[u] == low[u]:
            tmp = []
            while stack:
                top = stack.pop()
                tmp.append(top)
                on_stack[top] = False
                if top == u: break
            sccs.append(tmp)

    for i in range(n):
        if dfn[i] == -1: dfs(i)
    return sccs


def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    w = [0] + list(map(int, input().split()))
    v = [0] + list(map(int, input().split()))
    d = [0] + list(map(int, input().split()))

    sccs = tarjan_scc(d)
    num_scc = len(sccs)
    scc_id = [-1] * (n + 1)
    scc_w = [0] * num_scc
    scc_v = [0] * num_scc
    for i, scc in enumerate(sccs):
        for u in scc:
            scc_id[u] = i
            scc_w[i] += w[u]
            scc_v[i] += v[u]

    fa = list(range(num_scc))
    children = [[] for _ in range(num_scc)]
    for u, v in enumerate(d):
        u_scc = scc_id[u]
        v_scc = scc_id[v]
        if u_scc != v_scc:
            fa[u_scc] = v_scc
            children[v_scc].append(u_scc)
    for i in range(1, num_scc):
        if fa[i] == i:
            fa[i] = 0
            children[0].append(i)

    ## Tree DP
    dp = [[0] * (m + 1) for _ in range(num_scc)]
    # 在以节点 u 为根的子树中，选择总重量恰好（或不超过）j 的软件，所能获得的最大价值
    for u in range(num_scc - 1, -1, -1):

        for j in range(scc_w[u], m + 1):
            dp[u][j] = scc_v[u]

        for v in children[u]:
            # 分组背包核心逻辑：容量外层倒序，子树分配内层顺序
            for j in range(m, scc_w[u] - 1, -1):
                # k 至少需要提供 scc_w[v] 才有意义
                for k in range(scc_w[v], j - scc_w[u] + 1):
                    dp[u][j] = max(dp[u][j], dp[u][j-k] + dp[v][k])
    print(max(dp[0]))

if __name__ == '__main__':
    main()