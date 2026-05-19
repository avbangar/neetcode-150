# https://neetcode.io/problems/duplicate-integer/question?list=neetcode150


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return len(set(nums)) != len(nums)
        # also works but doesn't short curcuit

        hashSet = set()
        for i in nums:
            if i in hashSet:
                # short circuit, don't need else
                return True
            hashSet.add(i)
        return False
