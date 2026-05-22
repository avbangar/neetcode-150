class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean = ''.join(c.lower() for c in s if c.isalnum())
        # return clean == clean[::-1]

        clean = ''.join(c.lower() for c in s if c.isalnum())
        middleIndex = len(clean) // 2

        for i in range(0, middleIndex):
            front = clean[i]
            back = clean[-1 - i]

            if front != back:
                return False

        return True
