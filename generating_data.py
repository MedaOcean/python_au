import math
import random
import sys

months = ['2020-01', '2020-02', '2020-03', '2020-04', '2020-05', '2020-06', '2020-07', '2020-08', '2020-09', '2020-10',
          '2020-11', '2020-12']
points = ['118', '202', '119']
stuff = ['RK900', 'RK800', 'Richard', 'Gavin', 'Reed', 'Connor']
titles = ['date', 'resource', 'stuff_id', 'count']


def data_with_sin(c, i, m):
    lst = []
    a = 0
    d = 3.14 / 6
    while a < len(months):
        b = int((1 + math.sin(d)) * c)
        lst.append(b)
        a += 1
        d += 3.14 / 6
    h = 0
    res = []
    for j in months:
        if m == 0:
            s = '{}, {}, {}'.format(j, i, lst[h])
        else:
            s = '{}, {}, {}, {}'.format(j, i, m, lst[h])
        res.append(s)
        h += 1
    return res


def data_with_parabola(c, i, m):
    lst = []
    a = -6
    while a < len(months):
        b = int(((c + a) / 10) ** 2)
        lst.append(b)
        a += 1
    h = 0
    res = []
    for j in months:
        if m == 0:
            s = '{}, {}, {}'.format(j, i, lst[h])
        else:
            s = '{}, {}, {}, {}'.format(j, i, m, lst[h])
        res.append(s)
        h += 1
    return res


def data_with_ln(c, i, m):
    lst = []
    a = 2000
    lt = len(months) - int(len(months)/2)
    u = 0
    while u < lt:
        b = int(math.log((c + a), 2))
        lst.append(b)
        a += 1000
        u += 1
    h = 0
    res = []
    j = len(lst)
    for k in range(j):
        if m == 0:
            s = '{}, {}, {}'.format(months[k], i, lst[h])
        else:
            s = '{}, {}, {}, {}'.format(months[k], i, m, lst[h])
        h += 1
        res.append(s)
    return res


def forming_data(c, m):
    data = ''
    result = []
    for g in range(len(points)):
        d = g % 3
        if d == 0:
            result = data_with_sin(c, points[g], m)
            c += 1
        if d == 1:
            result = data_with_parabola(c, points[g], m)
            c += 10
        if d == 2:
            c += 1000
            result = data_with_ln(c, points[g], m)
            c += 200
        for j in result:
            data = '{}{}\n'.format(data, j)
    return data


def forming_data_with_stuff(c):
    result = ''
    for i in stuff:
        data_with_stuff = forming_data(c, i)
        result = '{}{}'.format(result, data_with_stuff)
        c += 5
    return result


def write_to_md_file(file_name, data):
    file = open(file_name, "w")
    file.write(data)


def main(a, m):
    c = random.randint(10, 30)
    m = int(m)
    data_with_title = ''
    if m == 0:
        data = forming_data(c, 0)
        data_with_title = '{},{},{}\n{}'.format(titles[0], titles[1], titles[3], data)
    if m == 1:
        data = forming_data_with_stuff(c)
        data_with_title = '{},{},{},{}\n{}'.format(titles[0], titles[1], titles[2], titles[3], data)
    write_to_md_file(a, data_with_title)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])


