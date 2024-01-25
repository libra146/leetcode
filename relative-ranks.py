import copy
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        if not score:
            return []
        m = {}
        r = ['Gold Medal', 'Silver Medal', 'Bronze Medal']
        s = copy.copy(score)
        s.sort(reverse=True)
        for index, a in enumerate(s, 1):
            if not r:
                m[a] = str(index)
            else:
                m[a] = r.pop(0)
        return [m[a] for a in score]

# leetcode submit region end(Prohibit modification and deletion)
