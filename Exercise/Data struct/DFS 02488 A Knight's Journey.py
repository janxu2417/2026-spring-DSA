def main():
    def pos_to_rank(x, y, m) -> int:
        return y + x * m

    def rank_to_pos(r: int, m: int) -> str:
        x = r // m
        y = r - x * m
        return dic[y] + str(x + 1)

    def dfs(k, x, y, n, m) -> None:
        nonlocal find
        if k == n * m + 1:
            for i in range(n * m):
                ans[flag[i]] = rank_to_pos(i, m)
            find = True
            return
        if find:
            return

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                r = pos_to_rank(nx, ny, m)
                if flag[r]: continue
                flag[r] = k
                dfs(k + 1, nx, ny, n, m)
                flag[r] = 0

    find = False
    flag = [1] + [0] * 25
    ans = ['', 'A1'] + [''] * 25
    dic = {i : chr(i + 65) for i in range(26)}
    directions = [(-1, -2), (1, -2), (-2, -1), (2, -1), (-2, 1), (2, 1), (-1, 2), (1, 2)]

    for _ in range(int(input())):
        n, m = map(int, input().split())
        find = False
        dfs(2, 0, 0, n, m)
        print(f'Scenario #{_ + 1}:')
        if find:
            print(''.join(ans[1:n * m + 1]))
        else:
            print('impossible')
        print('')

if __name__ == '__main__':
    main()