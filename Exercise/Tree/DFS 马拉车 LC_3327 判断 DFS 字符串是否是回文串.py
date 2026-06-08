from typing import List
class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        def dfs(node):
            for x in child[node]:
                dfs(x)
                size[node] += size[x]
            order.append(node)
            size[node] += 1
            return

        def expand(l, r, n):
            while 0 < l and r < n - 1 and pattern[l - 1] == pattern[r + 1]:
                l -= 1
                r += 1
            return (r - l) // 2

        def manacher():
            n = len(pattern)
            p = [0] * n
            center = right_most = 0
            for i in range(1, n):
                if i >= right_most:
                    p[i] = expand(i, i, n)
                else:
                    j = 2 * center - i
                    if i + p[j] < right_most:
                        p[i] = p[j]
                    else:
                        p[i] = expand(2 * i - right_most, right_most, n)
                if i + p[i] > right_most:
                    right_most = i + p[i]
                    center = i
            for r in range(m):
                i = order[r]
                l = r - size[i] + 1
                #print(i, l, r, p[r + l + 1])
                if p[r + l + 1] >= r - l + 1:
                    ans[i] = True
            return

        m = len(parent)
        child = [[] for _ in range(m)]
        for i in range(1, m):
            child[parent[i]].append(i)
        order = []
        size = [0] * m
        dfs(0)
        #print(order)
        #print([s[order[i]] for i in range(m)])
        pattern = '#' + '#'.join([s[order[i]] for i in range(m)]) + '#'
        ans = [False] * m
        manacher()
        return ans