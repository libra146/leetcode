from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [i for i in range(left, right + 1) if all('0' not in str(i) and i % int(a) == 0 for a in str(i))]
# leetcode submit region end(Prohibit modification and deletion)
