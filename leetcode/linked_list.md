
+ [Middle of the Linked List](#middle-of-the-linked-list)
+ [Palindrome Linked List](#palindrome-linked-list)
+ [Linked List Cycle](#linked-list-cycle)
+ [Intersection of Two Linked Lists](#intersection-of-two-linked-lists)<---end.markdown links--->

## Middle of the Linked List
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