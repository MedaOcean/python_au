
+ [#1](#1)
+ [#2](#2)
+ [#3](#3)<---end.markdown links--->

## #1

``` python
def get_char_freq (s: str)(подсчет количества одинаковых элементов):
    freq = {}
    for c in s:
        freq.get(c) = freq.get(c, 0)+1
    return freq
```

## 2

https://leetcode.com/problems/merge-two-sorted-lists/class Solution:

``` python
    sorted_list = ListNode()
    cur = sorted_list
    while l1 is not None and l2 is not None:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    if l1 is not None:
            cur.next = l1
    if l2 is not None:
            cur.next = l2
    return sorted_list.next
```

## #3

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