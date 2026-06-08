import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    t = 0
    while True:
        n = int(next(it))
        if n == 0:
            break
        t += 1
        print(f'Test case #{t}')
        pattern = next(it)
        lps = [0] * n
        length = 0
        for i in range(1, n):
            while length and pattern[length] != pattern[i]:
                length = lps[length - 1]
            if pattern[length] == pattern[i]:
                length += 1
            lps[i] = length
            d = i + 1 - lps[i]
            if lps[i] and (i + 1) % d == 0:
                print(i + 1, (i + 1) // d)
        print('')

if __name__ == '__main__':
    main()