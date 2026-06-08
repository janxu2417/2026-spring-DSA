import sys
from collections import defaultdict

def topo_sort(n, edges, in_deg):
    q = [i for i in range(n) if in_deg[i] == 0]
    est = [0] * n
    head = 0
    while head < len(q):
        u = q[head]
        head += 1
        for v, w in edges[u]:
            in_deg[v] -= 1
            if est[u] + w > est[v]:
                est[v] = est[u] + w
            if in_deg[v] == 0:
                q.append(v)
    if len(q) < n:
        return None, None
    return est, q

def get_critical_path(n, edges, in_deg):

    est, topo_order = topo_sort(n, edges, in_deg)
    if topo_order is None:
        return -1, None

    max_length = max(est)
    lst = [max_length] * n
    activity = defaultdict(list)
    for u in reversed(topo_order):
        for v, w in edges[u]:
            if lst[v] - w < lst[u]:
                lst[u] = lst[v] - w
            if est[u] + w == lst[v]:
                activity[u].append((v, w))

    return max_length, activity

def print_critical_path(u, activity, max_length):

    output = [u]

    def dfs(node, cnt):
        if cnt == max_length:
            print(*output, sep='->')
            return
        for v, w in sorted(activity[node]):
            output.append(v)
            dfs(v, cnt + w)
            output.pop()

    dfs(u, 0)

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])
    ptr = 2

    edges = [[] for _ in range(n)]
    in_deg = [0] * n
    for _ in range(m):
        u, v, w = map(int, data[ptr : ptr+3])
        edges[u].append((v, w))
        in_deg[v] += 1
        ptr += 3

    in_deg_copy = in_deg.copy()
    max_length, activity = get_critical_path(n, edges, in_deg_copy)

    if max_length == -1:
        print('No')
    else:
        print('Yes')
        print(max_length)
        for i in range(n):
            if in_deg[i] == 0:
                print_critical_path(i, activity, max_length)


if __name__ == "__main__":
    main()