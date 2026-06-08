from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        cnt = [0] * 26
        for c in p:
            cnt[ord(c) - 97] += 1
        n = len(p)
        ans = []
        lf = 0
        for i, c in enumerate(s):
            x = ord(c) - 97
            cnt[x] -= 1
            while cnt[x] < 0:
                cnt[ord(s[lf]) - 97] += 1
                lf += 1
            if i - lf + 1 == n:
                ans.append(lf)
        return ans