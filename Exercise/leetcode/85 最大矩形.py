from typing import List
class Solution:
    def monotonous_stack(self, m, h):
        q = [(-1, 0)]
        max_area = 0
        for i in range(m):
            while len(q) > 1 and q[-1][1] >= h[i]:
                hx = q.pop()[1]
                lf = q[-1][0] + 1
                tmp = hx * (i - lf)
                if max_area < tmp:
                    max_area = tmp
            q.append((i, h[i]))
        return max_area
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        h = [0] * (m + 1)
        ans = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    h[j] += 1
                else:
                    h[j] = 0
            ans = max(ans, self.monotonous_stack(m + 1, h))
        return ans

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(Solution().maximalRectangle(matrix))