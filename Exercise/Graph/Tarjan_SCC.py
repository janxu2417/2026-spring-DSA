import sys

sys.setrecursionlimit(200000)
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
                if top == u: break
            sccs.append(sorted(tmp))

    for i in range(1, n):
        if dfn[i] == -1: dfs(i)
    return sorted(sccs, key=lambda x: x[0])

def main():
    it = iter(sys.stdin.read().split())
    n, m = int(next(it)), int(next(it))
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = int(next(it)), int(next(it))
        graph[u].append(v)
    sccs = tarjan_scc(graph)
    print(len(sccs))
    for scc in sccs:
        print(*scc, sep=' ')

if __name__ == '__main__':
    main()