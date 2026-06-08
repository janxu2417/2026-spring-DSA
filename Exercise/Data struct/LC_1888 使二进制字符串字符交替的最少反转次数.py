class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        tmp0 = sum(1 if int(s[i]) == i % 2 else 0 for i in range(n))
        tmp1 = n - tmp0
        ans = min(tmp0, tmp1)
        if n & 1:
            for i in range(1, n):
                if s[i - 1] == '1': 
                    tmp0, tmp1 = tmp1 - 1, tmp0 + 1
                else:
                    tmp0, tmp1 = tmp1 + 1, tmp0 - 1
                ans = min(ans, tmp0, tmp1)
        return ans