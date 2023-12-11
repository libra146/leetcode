# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        index = 0
        l = len(s)
        ss = s[index]
        while ss:
            if ss not in ['(', '[', '{']:
                if not stack:
                    return False
                if ss == ')':
                    if stack[-1] != '(':
                        return False
                    else:
                        stack.pop()
                if ss == ']':
                    if stack[-1] != '[':
                        return False
                    else:
                        stack.pop()
                if ss == '}':
                    if stack[-1] != '{':
                        return False
                    else:
                        stack.pop()
            else:
                stack.append(ss)
            index += 1
            if index > l - 1:
                break
            ss = s[index]
        return not stack
# leetcode submit region end(Prohibit modification and deletion)
