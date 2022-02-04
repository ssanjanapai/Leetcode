class Solution:
    def isValid(self, s: str) -> bool:
        matches = {
            ')':'(',
            ']':'[',
            '}':'{',
        }
        stack = []
        for char in s:
            if char not in matches:
                stack.append(char)
            else:
                if not stack or stack.pop() != matches[char]: return False
        if stack: return False
        return True

y = Solution()
s="{}[]()"
u="{}["
print(y.isValid(s))
print(y.isValid(u))

