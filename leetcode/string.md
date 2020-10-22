
+ [Valid Anagram](#valid-anagram)
+ [Reverse String](#reverse-string)
+ [Reverse Vowels of a String](#reverse-vowels-of-a-string)
+ [Reverse Words in a String III](#reverse-words-in-a-string-iii)
+ [To Lower Case](#to-lower-case)<---end.markdown links--->

## Valid Anagram

https://leetcode.com/problems/valid-anagram/

``` python
def isAnagram(self, s: str, t: str) -> bool:
    a = list(s).sort()
    b = list(t).sort()
    if a == b and len(s) == len(t):
        return True
    else:
        return False
```

## Reverse String

https://leetcode.com/problems/reverse-string/

``` python
def reverseString(self, s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    s.reverse()
```

## Reverse Vowels of a String

https://leetcode.com/problems/reverse-vowels-of-a-string/

``` python
def reverseVowels(self, s: str) -> str:
    a = ['e', 'u', 'i', 'o', 'a']
    b = []
    c = list(s)
    d = len(c)
    for i in range(d):
        if c[i] in a:
            b.append(c[i])
    g = b
    b.reverse()
    h = list(s)
    for i in range(d):
        if h[i] in g:
            l = g.index(h[i])
            k = len(b)-1-l
            c[i] = b[k]
            h[i] = 0
    l = "".join(c)
    return(l)
```

## Reverse Words in a String III

https://leetcode.com/problems/reverse-words-in-a-string-iii/

``` python
def reverseWords(self, s: str) -> str:
    a = list(s.split(" "))
    b = []
    c = len(a)
    for i in range(c):
        d = a[i]
        e = list(d)
        e.reverse()
        k = "".join(e)
        b.append("{} ".format(k))
    r = "".join(b)
    r = r.rstrip(" ")
    return r
```

## To Lower Case

https://leetcode.com/problems/to-lower-case/

``` python
def toLowerCase(self, str: str) -> str:
    a = str.lower()
    return a
```