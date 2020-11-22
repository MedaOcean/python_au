import sys

def get_all_lines_from_file(file_name):
    file = open(file_name)
    syp = file.readlines()
    return syp
def write_to_file(file_name, solution):
    file = open(file_name, "w")
    file.write(solution)
    file.close
def get_points_and_lenght(str):
    str = str.split(' ')
    for i in range(len(str)):
            str[i] = int(str[i])
    a = str[0]
    b = str[1]
    c = str[2]
    d = str[3]
    e = str[4]
    f = str[5]
    l_1 = ((a - c) ** 2 + (b - d) ** 2) ** 0.5
    l_2 = ((a - e) ** 2 + (b - f) ** 2) ** 0.5
    l_3 = ((c - e) ** 2 + (d - f) ** 2) ** 0.5
    return (l_1, l_2, l_3)
def is_points_a_triangle(a, b, c):
     if a**2 > b**2 + c**2 or b**2 > a**2 + c**2 or c**2 > b**2 + a**2:
        return False
     else:
        return True
def is_points_isosceles_triangle(a, b, c):
    if a == b or b == c or a == c:
        return True
    else:
        return False
def square_of_triangle(a, b, c):
    p = (a+b+c)/2
    s = (p*(p-a)*(p-b)*(p-c))**0.5
    return s
def from_string_to_square(s):
    l_1, l_2, l_3 = get_points_and_lenght(s)
    if is_points_a_triangle(l_1, l_2, l_3) == True and is_points_isosceles_triangle(l_1, l_2, l_3) == True:
        return square_of_triangle(l_1, l_2, l_3)
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
    for f in range(len(c)):
            c[f] = int(c[f])
    d = freq.get(max(c))
    write_to_file(b, d)
if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])












