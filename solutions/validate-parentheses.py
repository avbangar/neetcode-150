class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        bracketsMap = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for char in s:
            if char in bracketsMap:
                if not stack or stack.pop() != bracketsMap[char]:
                    return False
            else:
                stack.append(char)

        return not stack
