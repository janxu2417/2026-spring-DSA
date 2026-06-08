from collections import deque
import sys
def main():
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    def bfs_check(h_limit):
        q = deque([(0, 0)])
        nonlocal bfs_id
        bfs_id += 1
        while q:
            ur, uc = q.popleft()
            if ur == n - 1 and uc == m - 1:
                return True
            hu = h[ur][uc]
            for t in range(4):
                vr, vc = ur + dr[t], uc + dc[t]
                if 0 <= vr < n and 0 <= vc < m:
                    idx = vr * m + vc
                    hv = h[vr][vc]
                    if vis[idx] != bfs_id and abs(hv - hu) <= h_limit:
                        vis[idx] = bfs_id
                        q.append((vr, vc))
        return False
    input = sys.stdin.readline
    n, m = map(int, input().split())
    h = [list(map(int, input().split())) for _ in range(n)]
    vis = [0] * (n * m)
    bfs_id = 0
    l = -1
    r = max(map(max, h))
    while r - l > 1:
        mid = (l + r) >> 1
        if bfs_check(mid): r = mid
        else: l = mid
    print(r)


if __name__ == '__main__':
    main()