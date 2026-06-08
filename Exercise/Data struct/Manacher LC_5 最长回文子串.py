class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            while 0 < l and r < n - 1 and s1[l - 1] == s1[r + 1]:
                l -= 1
                r += 1
            return (r - l) // 2

        s1 = '#' + '#'.join(s) + '#'
        n = len(s1)
        p = [0] * n
        center = right_most = 0
        pos = 0
        max_len = 0
        for i in range(1, n):
            if i >= right_most:
                p[i] = expand(i, i)
            else:
                j = 2 * center - i
                if i + p[j] < right_most:
                    p[i] = p[j]
                else:
                    p[i] = expand(2 * i - right_most, right_most)
            if i + p[i] > right_most:
                right_most = i + p[i]
                center = i
            if p[i] > max_len:
                max_len = p[i]
                pos = i
        return ''.join(s1[pos - max_len: pos + max_len + 1].split('#'))

