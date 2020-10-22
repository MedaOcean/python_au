
+ [Max Consecutive Ones](#max-consecutive-ones)
+ [Move Zeroes](#move-zeroes)<---end.markdown links--->

## Max Consecutive Ones

https://leetcode.com/problems/max-consecutive-ones/

``` python
def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    a = 0
    b = []
    c = len(nums)
    for i in range(c):
        if nums[i] == 1:
            a = a + 1
            b.append(a)
        else:
            a = 0
    return max(b)
```

## Move Zeroes

https://leetcode.com/problems/move-zeroes/

``` python
def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    a = nums.count(0)
    for i in range(len(nums)):
        b = nums.count(0)
        if b > 0:
            nums.remove(0)
    for i in range(a):
        nums.append(0)
```