import sys

def get_all_lines_from_file(file_name):
    file = open(file_name)
    syp = file.readlines()
    return syp
def write_to_file(file_name, solution):
    file = open(file_name, "w")
    file.write(solution)
    file.close
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def length(self,other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

class Triangle:
    def __init__(self, a, b, c):
        self.l1 = a
        self.l2 = b
        self.l3 = c

    def is_points_a_triangle(self):
        if self.l1 ** 2 > self.l2 ** 2 + self.l3 ** 2 or self.l2 ** 2 > self.l1 ** 2 + self.l3 ** 2 or self.l3 ** 2 > self.l2 ** 2 + self.l1 ** 2:
            return False
        else:
            return True

    def is_points_isosceles_triangle(self):
        if self.l1 == self.l2 or self.l2 == self.l3 or self.l1 == self.l3:
            return True
        else:
            return False

    def square_of_triangle(self):
        p = (self.l1 + self.l2 + self.l3) / 2
        s = (p * (p - self.l1) * (p - self.l2) * (p - self.l3)) ** 0.5
        return s
def right_input(s):
    if len(list(s.split())) != 6:
        return False
    else:
        return  True

def from_string_to_square(s):
    if right_input(s) is True:
        s=s.split()
        x1 = int(s[0])
        y1 = int(s[1])
        x2 = int(s[2])
        y2 = int(s[3])
        x3 = int(s[4])
        y3 = int(s[5])
        point1 = Point(x1, y1)
        point2 = Point(x2, y2)
        point3 = Point(x3, y3)
        triangle = Triangle(point1.length(point2), point2.length(point3), point3.length(point1))
        if triangle.is_points_a_triangle() == True and triangle.is_points_isosceles_triangle() == True:
            return triangle.square_of_triangle()
        else:
            return 0
def main (a,b):
    source_lines = get_all_lines_from_file(a)
    triangle = source_lines
    freq = {}
    for i in range(len(triangle)):
        a = from_string_to_square(triangle[i])
        freq[a] = triangle[i]
    c = list(freq.keys())
    d = freq.get(max(c))
    write_to_file(b, d)
if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])












