def main():
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    vis = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if matrix[i][j] and (i == 0 or i == n - 1 or j == 0 or j == m - 1) and vis[i][j] == 0:
                q = [(i, j)]
                vis[i][j] = 1
                while q:
                    r, c = q.pop()
                    for t in range(4):
                        nr = r + dr[t]
                        nc = c + dc[t]
                        if 0 <= nr < n and 0 <= nc < m and matrix[nr][nc] == 1 and vis[nr][nc] == 0:
                            vis[nr][nc] = 1
                            q.append((nr, nc))
    for row in vis:
        print(*row)

    return
if __name__ == '__main__':
    main()