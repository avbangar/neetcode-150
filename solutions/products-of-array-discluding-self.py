class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount = 0
        hasNonZero = False
        product = 1
        results: List[int] = []
        
        for n in nums:
            if n != 0:
                hasNonZero = True
                product = n * product
            else:
                zeroCount = zeroCount + 1

        if zeroCount > 1 or hasNonZero == False:
            return [0] * len(nums)
        
        for n in nums:
            if zeroCount == 1:
                if n == 0:
                    results.append(product)
                else:
                    results.append(0)
            else:
                results.append(int(product/n))
        
        return results
