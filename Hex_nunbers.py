import sys
def from_hex_to_decimal(num):
    return ord(num) - ord('A') + 10 if num >= 'A' and num <= 'F' else ord(num) - ord('0')
def from_decimal_to_hex(num):
    return chr(num + ord('A') - 10) if num > 9 else chr(ord('0') + num)
def title(s):
    a = s.upper()
    if a == s:
        return True
    else:
        return False
def positive(s):
    for i in range(len(s)):
        if from_hex_to_decimal(s[i])<0:
            return False
    return True

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def get(self, index: int) -> int:
        if index == 0:
            return self.head.val
        if index < 0 or index >= self.length:
            return -1
        elif index == self.length:
            return self.tail.val
        else:
            node = self.head
            c = 0
            while node is not None:
                if c == index:
                    return node.val
                node = node.next
                c += 1
            return -1

    def add_at_head(self, val):
        node = Node(val)
        self.length += 1
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def __init__(self, string):
        self.head = None
        self.length = 0
        for i in range(len(string)):
            self.add_at_head(string[i])
    def __str__(self):
        res = ""
        ptr = self.head
        while ptr:
            res += str(ptr.val) + ", "
            ptr = ptr.next
        res = res.strip(", ")
        if len(res):
            return "[" + res + "]"
        else:
            return "[]"
class HexNumber:
    def __init__(self, s):
        self.num=MyLinkedList(s)
        self.length=len(list(s))
    def add(self,other):
        c = 0
        sum = []
        if self.length >= other.length:
            a = other.length
            b=1
            h=self.length
            e=self.num
        else:
            a = self.length
            b = 2
            h = other.length
            e = other.num
        for i in range(a):
            num_1 = self.num.get(i)
            num_2 = other.num.get(i)
            num_1 = from_hex_to_decimal(num_1)
            num_2 = from_hex_to_decimal(num_2)
            amount = (num_1+num_2+c) % 16
            sum.append(amount)
            c = (num_1 + num_2 + c) // 16
        if h != a:
            for j in range(h-a):
                if c != 0:
                    k= from_hex_to_decimal(e.get(j+a))
                    amount = (k + c) % 16
                    sum.append(amount)
                    c = (k+ c) // 16
                else:
                    sum.append(e.get(j+a))
        sum.reverse()
        g=''.join(str(o) for o in sum)
        g=int(g)
        temp=[]
        while g//16 !=0:
            f=g//16
            t=g-16*f
            print(t)
            temp.append(from_decimal_to_hex(t))
            g = f
        temp.append(from_decimal_to_hex(g))
        temp.reverse()
        res=''.join(str(u) for u in temp)
        return res

def main(a, b):
    if title(a) is True and title(b) is True and positive(a) is True and positive(b) is True:
        num_1=HexNumber(a)
        num_2=HexNumber(b)
        res=num_1.add(num_2)

        print(res)
    else:
        print('Error')
if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])


