n = int(input())
files = []
for i in range(n):
    data = list(map(int, input().split()))
    files.append(set(data[1:]))
m = int(input())
for _ in range(m):
    find = input().split()
    t = find.index('1')
    a = files[t]
    for i in range(t + 1, n):
        if find[i] == '1':
            a = a & files[i]
    b = set()
    for i in range(n):
        if find[i] == '-1':
            b = b | files[i]
    file_name = list(a - b)
    if file_name:
        file_name.sort()
        print(' '.join(map(str, file_name)))
    else:
        print("NOT FOUND")