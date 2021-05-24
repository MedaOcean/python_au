import matplotlib.pyplot as plt
import sys

months = ['2020-01', '2020-02', '2020-03', '2020-04', '2020-05', '2020-06', '2020-07', '2020-08', '2020-09', '2020-10',
          '2020-11', '2020-12']
points = ['118', '202', '119']
stuff = ['RK900', 'RK800', 'Richard', 'Gavin', 'Reed', 'Connor']


def get_all_lines_from_file(file_name):
    file = open(file_name)
    syp = file.readlines()
    file.close
    return syp


def sorting_dictionary(lst):
    import operator
    lst.sort(key=operator.itemgetter('date'))
    return lst


def making_dictionary(s, s_1):
    lst = s.split(',')
    lst_1 = s_1.split(',')
    dic = {lst_1[0]: lst[0],
           lst_1[1]: lst[1][1:],
           lst_1[2]: lst[2][1:]}
    return dic


def making_dictionary_with_stuff(s, s_1):
    lst = s.split(',')
    lst_1 = s_1.split(',')
    dic = {lst_1[0]: lst[0],
           lst_1[2]: lst[2][1:],
           lst_1[1]: lst[1][1:],
           lst_1[3]: lst[3][1:]}
    return dic


def making_sorted_dictionary(s, s_1):
    lst_1 = []
    for i in s:
        i = i[:-1]
        h = making_dictionary(i, s_1)
        lst_1.append(h)
    result = sorting_dictionary(lst_1)
    return result


def making_sorted_dictionary_with_stuff(s, s_1):
    lst_1 = []
    for i in s:
        i = i[:-1]
        h = making_dictionary_with_stuff(i, s_1)
        lst_1.append(h)
    res = sorting_dictionary(lst_1)
    return res


def making_grafics(list_dict):
    for c in points:
        xdata = []
        ydata = []
        titl = '{}'.format(c)
        for a in list_dict:
            if int(a.get('resource')) == int(c):
                xdata.append(a.get('date'))
                ydata.append(int(a.get('count')))
        plt.plot(xdata, ydata, label=titl)
        plt.legend()
        plt.xlabel('Months')
        plt.ylabel('Number of caught deviants')


def making_grafics_with_stuff(lst_dict):
    for r in stuff:
        lst_1 = []
        tit = '{}'.format(r)
        for a in lst_dict:
            if a.get('stuff_id') == r:
                lst_1.append(a)
        making_grafics(lst_1)
        plt.title(tit)
        plt.show()


def main(c):
    data = get_all_lines_from_file(c)
    print(data)
    lst_titles = data[0].split(',')
    if len(lst_titles) == 3:
        sorted_data = making_sorted_dictionary(data[1:], data[0][:-1])
        making_grafics(sorted_data)
    else:
        sorted_data = making_sorted_dictionary_with_stuff(data[1:], data[0][:-1])
        making_grafics_with_stuff(sorted_data)


if __name__ == '__main__':
    main(sys.argv)