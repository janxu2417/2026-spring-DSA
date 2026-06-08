import sys
from collections import deque

sys.setrecursionlimit(10**5)
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
        for v in graph[u]:
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
                if top == u:
                    break
            sccs.append(tmp)
        return

    for i in range(1, n):
        if dfn[i] == -1:
            dfs(i)
    return sccs

def main():
    inf = 30000
    it = iter(sys.stdin.read().split())
    n, p = int(next(it)), int(next(it))
    can_visit = []
    cost = [inf] * (n + 1)
    for _ in range(p):
        idx = int(next(it))
        can_visit.append(idx)
        cost[idx] = int(next(it))
    graph = [[] for _ in range(n + 1)]
    for _ in range(int(next(it))):
        u, v = int(next(it)), int(next(it))
        graph[u].append(v)
    sccs = tarjan_scc(graph)

    num_scc = len(sccs)
    scc_id = [-1] * (n + 1)
    in_deg = [0] * num_scc
    mn = [inf] * num_scc

    for i, scc in enumerate(sccs):
        for u in scc:
            scc_id[u] = i
            mn[i] = min(mn[i], cost[u])

    dag = [set() for _ in range(num_scc)]
    for u in range(1, n + 1):
        scc_u = scc_id[u]
        for v in graph[u]:
            scc_v = scc_id[v]
            if scc_u != scc_v and scc_v not in dag[scc_u]:
                in_deg[scc_v] += 1
                dag[scc_u].add(scc_v)

    ans = 0
    opt = inf

    for idx in range(num_scc):
        if in_deg[idx] == 0:
            if mn[idx] < inf:
                ans += mn[idx]
            else:
                opt = min(opt, min(sccs[idx]))
    if opt == inf:
        print('YES')
        print(ans)
    else:
        print('NO')
        q = deque()
        vis = [False] * num_scc
        for u in can_visit:
            scc_u = scc_id[u]
            if not vis[scc_u]:
                q.append(scc_u)
                vis[scc_u] = True
        while q:
            u = q.popleft()
            for v in list(dag[u]):
                if not vis[v]:
                    vis[v] = True
                    q.append(v)
        for i, scc in enumerate(sccs):
            if vis[i] == False:
                opt = min(opt, min(scc))
        print(opt)

    # print(*sccs)

if __name__ == '__main__':
    main()