import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    while True:
        pattern = next(it)
        if pattern == '.':
            break
        n = len(pattern)
        lps = [0] * n
        length = 0
        for i in range(1, n):
            while length and pattern[length] != pattern[i]:
                length = lps[length - 1]
            if pattern[length] == pattern[i]:
                length += 1
            lps[i] = length
        d = n - lps[n - 1]
        if n % d == 0:
            print(n // d)
        else:
            print(1)

if __name__ == '__main__':
    main()