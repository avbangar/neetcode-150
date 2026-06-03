//https://neetcode.io/problems/non-cyclical-number

class Solution {
    private(set) var memo: Set<Int> = []

    func isHappy(_ n: Int) -> Bool {
        if n == 1 {
            return true
        } else if memo.contains(n) {
            return false 
        } else {
            memo.insert(n)
            var total = 0
            var num = n
            while num > 0 {
                let remainder = num % 10
                num /= 10   
                total += (remainder * remainder)              
            }
            return isHappy(total)
        }
    }
}
