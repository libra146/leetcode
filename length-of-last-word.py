class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        left = -1
        right = -1
        ss = list(s)
        if ss[-1] == ' ':
            while ss[right] == ' ':
                right -= 1
            left = right
        while abs(left) <= len(s) and ss[left] != ' ':
            left -= 1
        if right == -1:
            return len(ss[left + 1:])
        else:
            return len(ss[left + 1:right + 1])


if __name__ == '__main__':
    print(Solution().lengthOfLastWord('a '))
    # Solution().lengthOfLastWord("   fly me   to   the moon  ")
    # Solution().lengthOfLastWord("Hello World")
