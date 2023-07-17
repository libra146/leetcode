from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for index, a in enumerate(nums):
            if target - a in m:
                return [m[target - a], index]
            m[a] = index
