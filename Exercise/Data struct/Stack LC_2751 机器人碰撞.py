from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:

        n = len(healths)
        index = sorted(range(n), key=lambda i: positions[i])

        st = [0] * n
        ind = [0] * n
        ans = [0] * n
        top = -1

        for i in range(n):
            hi = healths[index[i]]
            di = directions[index[i]]
            if di == 'R':
                top += 1
                st[top] = hi
                ind[top] = index[i]
            else:
                while top >= 0 and hi > 0 and st[top] < hi:
                    hi -= 1
                    top -= 1
                if top >= 0:
                    if hi < st[top] and st[top] > 1:
                        st[top] -= 1
                    else:
                        top -= 1
                elif hi:
                    ans[index[i]] = hi

        for i in range(top + 1):
            ans[ind[i]] = st[i]
        return [x for x in ans if x]

if __name__ == '__main__':
    sol = Solution
