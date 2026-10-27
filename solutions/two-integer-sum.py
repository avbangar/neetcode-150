class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, v in enumerate(nums):
            goal = target - v
            try:
                j = nums.index(goal, i+1)
                return [i, j]
            except ValueError:
                continue
        return [-1, -1]
