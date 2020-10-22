
+ [Non-overlapping Intervals](#non-overlapping-intervals)
+ [Merge Intervals](#merge-intervals)
+ [Insert Interval](#insert-interval)<---end.markdown links--->

## Non-overlapping Intervals

https://leetcode.com/problems/non-overlapping-intervals/

``` python
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
```
## Merge Intervals

https://leetcode.com/problems/merge-intervals/

``` python
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
            m = [intervals[0]]
            for c in intervals:
                p = m[-1]
                if c[0] < = p[1]:
                    p[1] = max(p[1], c[1])
                else:
                    m.append(c)
            return(m)
```
## Insert Interval

https://leetcode.com/problems/insert-interval/

``` python
def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    r = []
    a = newInterval[0]
    b = newInterval[1]
    for s, e in intervals:
        if e < a or s > b:
            r.append([s, e])
        else:
            a = min(a, s)
            b = max(b, e)
    r + = [[a, b]]
    return(sorted(r))
```