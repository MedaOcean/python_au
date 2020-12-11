class ComplexNumber:
    def __init__(self, x, y):
        self.re = float(x)
        self.img = float(y)
    def add(self, other):
        return ComplexNumber(self.re+other.re, self.img+other.im)
    def sub(self, other):
        return ComplexNumber(self.re - other.re, self.img - other.im)
    def __str__(self):
        return '({0}+{1}i'.format(self.re, self.img)
    def __eq__(self, other):
        return True if ((self.re == other.re) and (self.img == other.img)) else False
    def __ne__(self, other):
        return True if ((self.re != other.re) and (self.img != other.img)) else False
    def mod(self):
        return (self.re**2+self.img**2)**0,5
    def multiplication(self, other):
        return ComplexNumber(self.re*other.re+self.img*other.im, self.re*other.im+self.img*other.re)
