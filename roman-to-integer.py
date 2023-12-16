# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
class Solution:
    def romanToInt(self, s: str) -> int:
        map_ = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, '': 0}
        res = 0
        ss = list(s)
        pre = ''
        while ss:
            a = ss.pop()
            if a in ['V', 'X', 'L', 'C', 'D', 'M']:
                if map_[a] < map_[pre]:
                    res -= map_[a]
                else:
                    res += map_[a]
            else:
                if pre in ['V', 'X', 'L', 'C', 'D', 'M']:
                    res -= map_[a]
                else:
                    res += map_[a]
            pre = a
        return res


if __name__ == '__main__':
    # print(Solution().romanToInt('III'))
    # print(Solution().romanToInt('IV'))
    print(Solution().romanToInt('LVIII'))
    print(Solution().romanToInt('MCMXCIV'))
