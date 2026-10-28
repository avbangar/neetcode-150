class Solution {
    func longestConsecutive(_ nums: [Int]) -> Int {
        guard !nums.isEmpty else { return 0 }

        let uniqueNums = Set(nums)
        var longestStreak = 1

        for x in uniqueNums {
            if !uniqueNums.contains(x - 1) {
                var currentStreak = 1
                var nextValue = x + 1
                
                while uniqueNums.contains(nextValue) {
                    currentStreak += 1
                    nextValue += 1
                }

                longestStreak = max(longestStreak, currentStreak)
            }
        }

        return longestStreak
    }
}
