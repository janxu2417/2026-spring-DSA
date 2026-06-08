import sys
from collections import deque

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    c = [0]
    bias = [0]
    for i in range(n):
        ci, ui = map(int, input().split())
        c.append(ci)
        bias.append(ui)
    adj = [[] for _ in range(n + 1)]
    in_deg = [0] * (n + 1)
    out_deg = [0] * (n + 1)
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        out_deg[u] += 1
        in_deg[v] += 1

    q = deque([i for i in range(1, n + 1) if in_deg[i] == 0])
    cnt = 0
    while q:
        u = q.popleft()
        cnt += 1
        if c[u] < 0:
            c[u] = 0
        for v, w in adj[u]:
            in_deg[v] -= 1
            c[v] += c[u] * w
            if in_deg[v] == 0:
                c[v] -= bias[v]
                q.append(v)

    candidates = [(i, c[i]) for i in range(1, n + 1) if out_deg[i] == 0 and c[i] > 0]
    if cnt < n or len(candidates) == 0:
        print('NULL')
    else:
        candidates.sort()
        for node in candidates:
            print(*node)

if __name__ == '__main__':
    main()