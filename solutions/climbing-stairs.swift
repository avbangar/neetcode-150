//https://neetcode.io/problems/climbing-stairs

class Solution {
    private var memo: [Int: Int] = [
        1: 1, 
        2: 2
    ]

    func climbStairs(_ n: Int) -> Int {
        guard n > 0 else {
            return 0
        }
        
        if memo[n] == nil {
            let minus1 = climbStairs(n-1)
            let minus2 = climbStairs(n-2)

            memo[n] = minus1 + minus2
        }

        return memo[n]!
    }
}
