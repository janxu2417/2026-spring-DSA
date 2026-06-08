def solve(lines):
    i = 0
    n = len(lines)
    def process_dir(level):
        nonlocal i
        files = []
        while i < n:
            line = lines[i]
            i += 1
            if line == ']' or line == '*':
                for f in sorted(files):
                    print("|     " * level + f)
                return

            if line.startswith('d'):
                print("|     " * (level + 1) + line)
                process_dir(level + 1)
            elif line.startswith('f'):
                files.append(line)

    process_dir(0)

def main():
    datasets = []
    cur = []
    while True:
        s = input().strip()
        if s == "#":
            break
        cur.append(s)
        if s == '*':
            datasets.append(cur)
            cur = []

    cnt = 1
    while cnt <= len(datasets):
        print(f'DATA SET {cnt}:')
        print('ROOT')
        solve(datasets[cnt - 1])
        print("")
        cnt += 1

if __name__ == '__main__':
    main()