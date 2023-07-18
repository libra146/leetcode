class Solution:
    j = False

    def addStrings(self, num1: str, num2: str) -> str:
        result = ''
        num2 = list(num2[::-1])
        num1 = list(num1[::-1])
        if len(num2) > len(num1):
            max_num = num2
            min_num = num1
        else:
            max_num = num1
            min_num = num2
        for i, v in enumerate(max_num):
            a1 = max_num[i]
            a2 = min_num[i] if i < len(min_num) else ''
            result += self.add(a1 if a1 else 0, a2 if a2 else 0)
        return result[::-1] if not self.j else '1' + result[::-1]

    def add(self, v1, v2):
        value = int(v1) + int(v2) + (1 if self.j else 0)
        self.j = False
        if value >= 10:
            self.j = True
            value -= 10
        else:
            self.j = False
        return str(value)


class Solution2:

    def addStrings(self, num1: str, num2: str) -> str:
        res = ''
        carry = 0
        len1, len2 = len(num1) - 1, len(num2) - 1
        while len1 >= 0 or len2 >= 0:
            v1 = num1[len1] if len1 >= 0 else 0
            v2 = num2[len2] if len2 >= 0 else 0
            value = int(v1) + int(v2) + carry
            carry = value // 10
            res = str(value % 10) + res
            len1 -= 1
            len2 -= 1
        return res if not carry else '1' + res


if __name__ == '__main__':
    print(Solution2().addStrings('11', '123'))
