from collections import Counter
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        w1 = Counter(words1)
        w2 = Counter(words2)
        res = 0
        for k, v in w1.items():
            if w1[k] == 1 and 1 == w2[k]:
                res += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
