//https://neetcode.io/problems/single-number

class Solution {
    func singleNumber(_ nums: [Int]) -> Int {
        var singleton = 0 

        for num in nums {
            singleton ^= num
        }

        return singleton
    }
}
