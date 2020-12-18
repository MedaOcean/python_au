triangle = "0 1 0 2 0 3"
class Triangle:
    def __init__(self, string):
        self.list = string.split(" ")
    def get_points_and_lenght(self):
        lowy = self.list
        l = len(lowy)
        for i in range(l):
            self.list[i] = int((self.list)[i])
        a = self.list[0]
        b = self.list[1]
        c = self.list[2]
        d = self.list[3]
        e = self.list[4]
        f = self.list[5]
        l_1 = ((a - c) ** 2 + (b - d) ** 2) ** 0.5
        l_2 = ((a - e) ** 2 + (b - f) ** 2) ** 0.5
        l_3 = ((c - e) ** 2 + (d - f) ** 2) ** 0.5
        return (l_1, l_2, l_3)
s = Triangle(triangle)
k = s.get_points_and_lenght()
print(k)