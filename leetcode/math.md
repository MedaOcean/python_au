
+ [Reverse Integer](#reverse-integer)
+ [Palindrome Number](#palindrome-number)
+ [Fizz Buzz](#fizz-buzz)
+ [Base 7](#base-7)
+ [Fibonacci Number](#fibonacci-number)
+ [Largest Perimeter Triangle](#largest-perimeter-triangle)
+ [Sqrt(x)](#sqrtx)<---end.markdown links--->

## Reverse Integer

https://leetcode.com/problems/reverse-integer/

``` python
def reverse(self, x: int) -> int:
    def reverse_for_positive(h):
        s = str(h)
        a = len(s)
        b = 0
        for i in range(0, a):
            d = s[i]
            e = int(d)
            b = b + e*(10**i)
        return b
    if x < 0:
        m = -x
        n = reverse_for_positive(m)
        g = -n
    else:
        g = reverse_for_positive(x)
    return g
```

## Palindrome Number

https://leetcode.com/problems/palindrome-number/

``` python
def isPalindrome(self, x: int) -> bool:
    def reverse_for_positive(h):
        s = str(h)
        a = len(s)
        b = 0
        for i in range(0, a):
            d = s[i]
            e = int(d)
            b = b + e*(10**i)
        return b
    if x < 0:
        return False
    else:
        g = reverse_for_positive(x)
        if g == x:
            return True
        else:
            return False  
```

## Fizz Buzz

https://leetcode.com/problems/fizz-buzz/

``` python
def fizzBuzz(self, n: int) -> List[str]:
    a = []
    for i in range(1, n+1):
        if i % 3 == 0:
            if i % 5 == 0:
                a.append("{}".format("FizzBuzz"))
            else:
                a.append("{}".format("Fizz"))
        else:
            if i % 5 == 0:
                a.append("{}".format("Buzz"))
            else:
                a.append(str(i))
    return a
```

## Base 7

https://leetcode.com/problems/base-7/

``` python
def convertToBase7(self, num: int) -> str:
    def base_7_for_positive(h):
        a = []
        l = len(str(h))
        for i in range(l):
            m = h//7
            n = h % 7
            a.append(n)
            h = m
        b = 0
        for i in range(0, l):
            d = a[i]
            e = int(d)
            b = b + e*(10**i)
        return b
    if num < 0:
        k = -num
        j = base_7_for_positive(k)
        g = -j
    else:
        g = base_7_for_positive(num)
    return str(g)
```

## Fibonacci Number

https://leetcode.com/problems/fibonacci-number/

``` python
def fib(self, N: int) -> int:
    f = 0
    if N < 2:
        f = N
    else:
        prev = 0
        cur = 1
        next = 0
        for i in range(N-1):
            next = cur + prev
            prev = cur
            cur = next
        f = cur
        return f
```

## Largest Perimeter Triangle

https://leetcode.com/problems/largest-perimeter-triangle/

``` python
def largestPerimeter(self, A: List[int]) -> int:
    a = sorted(A)
    c = len(a)
    b = []
    for i in range(c-2):
        if a[i+2] < a[i] + a[i+1]:
            d = a[i+2]+a[i] + a[i+1]
            b.append(d)
        else:
            b.append(0)
    e = max(b)
    return e
```

## Sqrt(x)

https://leetcode.com/problems/sqrtx/

``` python
def mySqrt(self, x: int) -> int:
    i = x // 2
    while (i+1)*(i+1) >= x and i*i >= x:
        i = i - 1
    while (i+1)*(i+1) <= x and i*i <= x:
        i = i + 1
    return(i)
```