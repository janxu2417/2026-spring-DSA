def find(fa, x):
    if fa[x] != x:
        fa[x] = find(fa, fa[x])
    return fa[x]

def main():
    n = int(input())
    edges = []
    fa = list(range(n))
    for i in range(n - 1):
        data = input().split()
        for j in range(2, len(data), 2):
            edges.append((int(data[j + 1]), i, ord(data[j]) - ord('A')))
    edges.sort()
    ans = 0
    cnt = 0
    for edge in edges:
        w, u, v = edge
        u, v = find(fa, u), find(fa, v)
        if u != v:
            fa[u] = v
            ans += w
            cnt += 1
        if cnt == n - 1:
            break
    print(ans)

if __name__ == '__main__':
    main()