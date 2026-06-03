//https://neetcode.io/problems/meeting-schedule

/**
 * Definition of Interval:
 * class Interval {
 *     var start: Int
 *     var end: Int
 *     init(_ start: Int, _ end: Int) {
 *         self.start = start
 *         self.end = end
 *     }
 * }
 */

class Solution {
    func canAttendMeetings(_ intervals: [Interval]) -> Bool {
        guard intervals.count > 1 else {
            return true
        }

        let sorted = intervals.sorted { $0.start < $1.start}

        for (current, next) in zip(sorted, sorted.dropFirst()) {
            if next.start < current.end {
                return false
            }
        }  

        return true
    }
}
