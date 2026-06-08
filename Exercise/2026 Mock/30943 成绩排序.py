def main():
    n, m = map(int, input().split())
    d = [[-1] * n for _ in range(n)]
    for _ in range(m):
        x, y, z = map(int, input().split())
        d[x][y] = z
        d[y][x] = 1 - z
    if m < n - 1:
        print(0)
        return

    # ----floyd-------
    for k in range(n):
        for i in range(n):
            if d[i][k] == -1:
                continue
            for j in range(n):
                if d[i][k] == d[k][j]:
                    d[i][j] = d[i][k]
    ans = 0
    for i in range(n):
        if d[i].count(-1) == 1:
            ans += 1
    print(ans)

    return
if __name__ == '__main__':
    main()