def main():
    while True:
        try:
            n = int(input())
            edges = [list(map(int, input().split())) for _ in range(n)]

            inf = float('inf')
            dis = [inf] * n
            flag = [False] * n

            dis[0] = 0
            ans = 0

            for _ in range(n):
                # 步骤 A：在尚未加入 MST 的节点中，找到距离集合最近的节点 u
                u = -1
                min_dist = inf
                for i in range(n):
                    if not flag[i] and dis[i] < min_dist:
                        min_dist = dis[i]
                        u = i
                # 步骤 B：将 u 加入 MST，并累加边权
                flag[u] = True
                ans += dis[u]
                # 步骤 C：用刚加入的节点 u，去更新其他未访问节点的距离
                for v in range(n):
                    if not flag[v] and edges[u][v] < dis[v]:
                        dis[v] = edges[u][v]
            print(ans)
        except EOFError:
            break

if __name__ == '__main__':
    main()