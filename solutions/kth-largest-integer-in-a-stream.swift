https://neetcode.io/problems/kth-largest-integer-in-a-stream

import Collections

final class KthLargest {
    private(set) var nums = Heap<Int>()
    private let k: Int

    init(_ k: Int, _ nums: [Int]) {
        self.k = k
        for num in nums {
            add(num)
        }
    }

    @discardableResult
    func add(_ val: Int) -> Int {
        if nums.count < k {
            nums.insert(val)
        } else if let smallestInHeap = nums.min, val > smallestInHeap {
            _ = nums.popMin()
            nums.insert(val)
        }
        
        return nums.min ?? 0 
    }
}
