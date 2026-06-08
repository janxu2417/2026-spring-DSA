from heapq import heappush, heappop

def dijkstra(m, steps):
    dis = [-1] * m
    dis[1] = 1
    q = [(1, 1)]
    while q:
        disu, u = heappop(q)
        if disu > dis[u]: continue
        for w in steps:
            v = (u + w) % m
            if dis[v] == -1 or dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
                heappush(q, (dis[v], v))
    return dis

def main():
    h = int(input())
    steps = set(map(int, input().split()))
    m = min(steps)
    if m == 1:
        print(h)
    else:
        dis = dijkstra(m, tuple(steps))
        ans = 0
        for i in range(m):
            if 0 < dis[i] <= h:
                ans += (h - dis[i]) // m + 1
        print(ans)

if __name__ == '__main__':
    main()