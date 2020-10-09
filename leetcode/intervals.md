# Intervals

+ [Non-overlapping Intervals](#non-overlapping-intervals)

## Non-overlapping Intervals

https://leetcode.com/problems/non-overlapping-intervals/


'''python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        p = intervals[0]
        deleted = 0
        for c in range(1, len(intervals)):
            s, e = intervals[c]
            if s < p[1]:
                deleted + = 1
                if e < p[1]:
                    p = intervals[c]
            else:
                p = intervals[c]
        return(deleted)
'''
