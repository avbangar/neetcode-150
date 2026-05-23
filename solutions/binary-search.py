class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            middle = (end + start)//2

            if nums[middle] > target:
                end = middle - 1
            elif nums[middle] < target:
                start = middle + 1
            elif nums[middle] == target:
                return middle

        return -1
