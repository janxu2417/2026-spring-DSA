import sys
from heapq import heapreplace

def main():
    input = sys.stdin.readline
    outline = []
    for _ in range(int(input())):
        m, n = map(int, input().split())
        res = sorted(list(map(int, input().split())))
        q = []
        for _ in range(m - 1):
            row = sorted(list(map(int, input().split())))
            h = [(res[i] + row[0], 0) for i in range(n)]
            # heapify(h)
            for i in range(n):
                curr_sum, idx = h[0]
                res[i] = curr_sum
                if idx + 1 < n:
                    nxt_sum = curr_sum + row[idx + 1] - row[idx]
                    heapreplace(h, (nxt_sum, idx + 1))

        outline.append(' '.join(map(str, res)))

    sys.stdout.write("\n".join(outline))


if __name__ == '__main__':
    main()