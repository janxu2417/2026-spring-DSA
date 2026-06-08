# from itertools import accumulate
#
# nums = [3,1,5,2,4]
#
# pre_max = list(accumulate(nums, max))
# print(pre_max)

s = input()
ans = 0
dic = {chr(x + ord('A')) : x + 1 for x in range(26)}

for c in s:
    ans = ans * 26 + dic[c]
print(ans)