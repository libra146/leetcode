from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.res = 0
        self.used = [False] * len(nums)
        self.backtrack(nums, [], 0)
        return self.res + self.xor(nums)

    def xor(self, nums):
        if len(nums) == 1:
            return nums[0]
        n = nums[0]
        for a in nums[1:]:
            n ^= a
        return n

    def backtrack(self, nums, track, i):
        if 1 <= len(track) < len(self.used):
            self.res += self.xor(track)
        for b in range(i, len(nums)):
            if self.used[b]:
                continue
            track.append(nums[b])
            self.used[b] = True
            self.backtrack(nums, track, b + 1)
            self.used[b] = False
            track.pop()


if __name__ == '__main__':
    print(Solution().subsetXORSum([1, 3]))
    print(Solution().subsetXORSum([5, 1, 6]))
    # print(Solution().subsetXORSum([3, 4, 5, 6, 7, 8]))
