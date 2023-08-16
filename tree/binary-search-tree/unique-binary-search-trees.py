class Solution:
    m = None

    def numTrees(self, n: int) -> int:
        self.m = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        return self.count(1, n)

    def count(self, lo, hi):
        if lo > hi:
            return 1
        res = 0
        if self.m[lo][hi] != 0:
            return self.m[lo][hi]
        for a in range(lo, hi + 1):
            left = self.count(lo, a - 1)
            right = self.count(a + 1, hi)
            res += left * right
        self.m[lo][hi] = res
        return res
