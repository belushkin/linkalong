from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l, h, m = 0, len(nums) - 1, len(nums) >> 1

        while h - l > 1:
            if sum(1 for i in nums if i <= m) > m:
                h = m
            else:
                l = m

            m = (l + h + 1) >> 1
        return m


solution = Solution()
print(solution.findDuplicate([1, 3, 4, 2, 2]))
# print(solution.findDuplicate([1, 4, 2, 2]))
