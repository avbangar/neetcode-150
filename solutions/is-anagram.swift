//https://neetcode.io/problems/is-anagram

class Solution {
    func isAnagram(_ s: String, _ t: String) -> Bool {
        guard s.count == t.count else { return false }
        
        var memo: [Character: Int] = [:]
        
        for char in s {
            memo[char, default: 0] += 1
        }
        
        for char in t {
            if let count = memo[char], count > 0 {
                memo[char] = count - 1
            } else {
                return false
            }
        }

        return true
    }
}

