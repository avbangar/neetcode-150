class Solution {
    func twoSum(_ numbers: [Int], _ target: Int) -> [Int] {
        var leftIndex = 0
        var rightIndex = numbers.count - 1
        var total: Int { numbers[leftIndex] + numbers[rightIndex] }

        while total != target {
            if total > target {
                rightIndex -= 1
            } else {
                leftIndex += 1
            }
        }

        return [leftIndex + 1, rightIndex + 1]
    }
}
