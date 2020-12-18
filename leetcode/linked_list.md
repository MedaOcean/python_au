
+ [Middle of the Linked List](#middle-of-the-linked-list)
+ [Palindrome Linked List](#palindrome-linked-list)
+ [Linked List Cycle](#linked-list-cycle)
+ [Intersection of Two Linked Lists](#intersection-of-two-linked-lists)
+ [Reverse Linked List](#reverse-linked-list)
+ [Middle of the Linked List](#middle-of-the-linked-list)
+ [Merge Two Sorted Lists](#merge-two-sorted-lists/class Solution)
+ [Remove Nth Node From End of List](#remove-nth-node-from-end-of-list)
+ [Linked List Cycle II](#linked-list-cycle-ii)
+ [Sort List](#sort-list)<---end.markdown links--->


## Middle of the Linked List

https://leetcode.com/problems/middle-of-the-linked-list/

``` python
def middleNode(self, head: ListNode) -> ListNode:
    node = head
    c = 0
    while node:
        node = node.next
        c + = 1
    for i in range(0, c//2):
        head = head.next
    return(head)
```

## Palindrome Linked List

https://leetcode.com/problems/palindrome-linked-list/

``` python
def isPalindrome(self, head: ListNode) -> bool:
    t = head
    l = 1
    while t and t.next:
        t = t.next
        l + = 1
    s = head
    f = head
    p = None
    while f and f.next:
        f = f.next.next
        n = s.next
        s.next = p
        p = s
        s = n
    if l % 2 != 0:
        n = n.next
    while n and p:
        if p.val != n.val:
            return False
        p = p.next
        n = n.next
    return True
```

## Linked List Cycle

https://leetcode.com/problems/linked-list-cycle/

``` python
def hasCycle(self, head: ListNode) -> bool:
    if not head.next:
        return(False)
    f = head
    s = f
    while f and f.next:
        if f.next == s:
            return(True)
        s = s.next
        f = f.next.next
    return(False)
```

## Intersection of Two Linked Lists

https://leetcode.com/problems/intersection-of-two-linked-lists/

``` python
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    s=headA
    f=headB
    while s!=f:
        if s is None:
            s=headB
        else:
            s=s.next
        if f is None:
            f=headA
        else:
            f=f.next
    return(s)
```

## Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/

``` python
def reverseList(self, head: ListNode) -> ListNode:
    prev = None
    cur = head
    while cur is not None:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev
```

## Middle of the Linked List

https://leetcode.com/problems/middle-of-the-linked-list/

``` python
def middleNode(self, head: ListNode) -> ListNode:
    node = head
    c = 0
    while node:
        node = node.next
        c + = 1
    for i in range(0, c//2):
        head = head.next
    return(head)
```

## Merge Two Sorted Lists

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

## Remove Nth Node From End of List

https://leetcode.com/problems/remove-nth-node-from-end-of-list/

``` python
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    a = 0
    cur = head
    while cur.next is not None:
        a += 1
        cur = cur.next
    if a < n and n < 0:
        return []
    else:
        if n == 0:
            head = head.next
        else:
            prev = head
            cur = head.next
            c = 0
            while c < n:
                prev = cur
                cur = cur.next
                c += 1
            prev.next = cur.next
        return head
```

## Linked List Cycle II

https://leetcode.com/problems/linked-list-cycle-ii/

``` python
def detectCycle(self, head: ListNode) -> ListNode:
    dict = {}
    cur = head
    while cur is not None:
        if cur in dict:
            return cur
        else:
            dict[cur] = None
            cur = cur.next
    return None
```

## Sort List

https://leetcode.com/problems/sort-list/

``` python
def sortList(self, head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head
    else:
        lst = []
        while head is not None:
            lst.append(head.val)
            head = head.next
        lst.sort()
        cur = ListNode()
        temp = cur
        for i in lst:
            temp.next = ListNode(i)
            temp = temp.next
        temp.next = None
        return cur.next
```
