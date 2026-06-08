import sys
# from collections import deque

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
            sccs.append(tmp)

    for i in range(1, n):
        if dfn[i] == -1: dfs(i)
    return sccs

def build_dag(n, graph, sccs):
    num_scc = len(sccs)
    scc_id = [-1] * n
    for i, scc in enumerate(sccs):
        for u in scc:
            scc_id[u] = i

    dag = [set() for _ in range(num_scc)]
    in_degree = [0] * num_scc
    out_degree = [0] * num_scc
    for u, neighbors in enumerate(graph):
        for v in neighbors:
            u_scc = scc_id[u]
            v_scc = scc_id[v]
            if u_scc != v_scc and v_scc not in dag[u_scc]:
                dag[scc_id[u]].add(scc_id[v])
                in_degree[scc_id[v]] += 1
                out_degree[scc_id[u]] += 1

    return dag, in_degree, out_degree, scc_id

def process_dag(n, graph, in_degree, out_degree):
    # print(in_degree, out_degree)
    # for u, edge in enumerate(graph):
    #     print(f'{u} -> {edge}')
    zero_in = 0
    zero_out = 0
    single = 0
    for node in range(n):
        if in_degree[node] == 0:
            zero_in += 1
        if out_degree[node] == 0:
            zero_out += 1

    print(zero_in)

    print(max(zero_in, zero_out) if n > 1 else 0)

def main():
    it = iter(sys.stdin.read().split())
    n = int(next(it))
    graph = [[] for _ in range(n + 1)]
    for u in range(1, n + 1):
        v = int(next(it))
        while v:
            graph[u].append(v)
            v = int(next(it))
    sccs = tarjan_scc(graph)
    # for scc in sccs:
    #     print(*scc, sep=' ', end = ' **\n')

    dag, in_degree, out_degree, scc_id = build_dag(n + 1, graph, sccs)

    process_dag(len(sccs), dag, in_degree, out_degree)

if __name__ == '__main__':
    main()