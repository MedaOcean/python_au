
+ [Max Consecutive Ones](#max-consecutive-ones)
+ [Move Zeroes](#move-zeroes)
+ [Reshape the Matrix](#reshape-the-matrix)
+ [Image Smoother](#image-smoother)
+ [Flipping an Image](#flipping-an-image)
+ [Transpose Matrix](#transpose-matrix/solution)
+ [Squares of a Sorted Array](#squares-of-a-sorted-array)<---end.markdown links--->

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

## Reshape the Matrix

https://leetcode.com/problems/reshape-the-matrix/

``` python
def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
    l = len(nums)
    a = 0
    b = r*c
    for d in range(l):
        a = a + len(nums[d])
    if a != b:
        return nums
    else:
        lst = []
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                lst.append(nums[i][j])
        res = []
        for m in range(0, len(lst), c):
            res.append(lst[m:m+c])
    return res
```

## Image Smoother

https://leetcode.com/problems/image-smoother/

``` python
def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
    a, b = len(M), len(M[0])
    sums = [[0] * b for _ in range(a)]
    for i in range(a):
        for c in range(b):
            sums[i][c] = sum(M[i][max(0, c-1):c+2])
    for r in range(a):
        for c in range(b):
            total = sums[i][c]
            sum_count = 3 if c != 0 and c != b - 1 else min(b, 2)
            total_count = sum_count
            if i != 0:
                total += sums[i-1][c]
                total_count += sum_count
            if i != a - 1:
                total += sums[r+1][c]
                total_count += sum_count
            M[r][c] = floor(total / total_count)
    return M
```

## Flipping an Image

https://leetcode.com/problems/flipping-an-image/

``` python
def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
    res = []
    a = len(A)
    b = len(A[0])
    for i in range(a):
        A[i].reverse()
        for j in range(b):
            if A[i][j] == 0:
                A[i][j] = 1
            else:
                A[i][j] = 0
        res.append(A[i])
    return res
```

## Transpose Matrix

https://leetcode.com/problems/transpose-matrix/solution/

``` python
def transpose(self, A: List[List[int]]) -> List[List[int]]:
    a=len(A[0])
    b=len(A)
    res=[]
    for i in range(a):
        lst=[]
        for j in range (b):
            lst.append(A[j][i])
        res.append(lst)
    return res
```

## Squares of a Sorted Array

https://leetcode.com/problems/squares-of-a-sorted-array/

``` python
def sortedSquares(self, A: List[int]) -> List[int]:
    def get_first_nonegative(A: List[int]):
        for i, val in enumerate(A):
            if val >=0:
                return i
        return -1
    ind = get_first_nonegative(A)
    if ind == -1:
        return [x**2 for x in A[::-1]]
    elif ind == 0:
        return [x**2 for x in [A]]
    else:
        left, right = ind-1, ind
        length = len(A)
        res = []
        while left >= 0 and right < length:
                if A[left]**2 < A[right]**2:
                    res.append(A[left]**2)
                    left -= 1
                else:
                    res.append(A[right]**2)
                    right += 1
        while left >= 0:
                res.append(A[left]**2)
                left -= 1
        while right < length:
                res.append(A[right]**2)
                right += 1
    return res
```