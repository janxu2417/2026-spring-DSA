import sys

def main():
    it = iter(sys.stdin.read().split())
    n = int(next(it))
    m = int(next(it))
    root = int(next(it))
    edge = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        x = int(next(it))
        y = int(next(it))
        edge[x].append(y)
        edge[y].append(x)

    def build_tree():
        nonlocal root
        st = [(root, 0)]
        while st:
            node, pre = st.pop()
            depth[node] = depth[pre] + 1
            parent[node] = pre
            for child in edge[node]:
                if child != pre:
                    st.append((child, node))

    parent = [0] * (n + 1)
    depth = [0] * (n + 1)
    fa = [parent]
    build_tree()
    i = 1
    while (1 << i) < n:
        last = fa[-1]
        tmp = [0]
        for j in range(1, n + 1):
            if last[j] == 0:
                tmp.append(0)
            else:
                tmp.append(last[last[j]])
        fa.append(tmp)
        i += 1

    def get_lca(x: int, y: int) -> int:
        if depth[x] < depth[y]:
            x, y = y, x
        d = depth[x] - depth[y]

        i = 0
        while d > 0:
            if d & 1:
                x = fa[i][x]
            d >>= 1
            i += 1
        if x == y:
            return x
        i = len(fa) - 1
        while i >= 0:
            if fa[i][x] != fa[i][y]:
                x = fa[i][x]
                y = fa[i][y]
            i -= 1
        return fa[0][x]

    ans = []
    for _ in range(m):
        x = int(next(it))
        y = int(next(it))
        ans.append(str(get_lca(x, y)))
    sys.stdout.write('\n'.join(ans))


if __name__ == '__main__':
    main()
