import requests
import json
GITHUB_TOKEN = '1ee7ae9c9d2d53b67a21772de76c572bfc54d850'
notice = 'Everything is fine'
notice_1 = 'Title is not suppose to be empty line'
notice_2 = 'Title suppose to contain more than 2 words'
notice_3 = 'Title is suppose to contain project name in capital letters and group number separated by a - as a first world'
project_names = ['VERIFICATION', 'GENERATOR', 'LEETCODE', 'HEXNUMBER', 'ITERATOR', 'TRIANGLE', 'REQUESTS']
notice_4 = 'Title is suppose to contain project name in capital letters'
notice_5 = 'Title is suppose to contain project name in CAPITAL letters'
numbers_of_group = ['1021', '1022', '1013']
notice_6 = 'Title is suppose to contain number of group without punctuation marks'
words_of_action = ['Added', 'Fixed', 'Created']
notice_7 = 'Title is suppose to contain action taken'


def get_headers():
    return {'Authorization': 'token {}'.format(GITHUB_TOKEN), 'Content-Type': "application/json"}


def get_user_pull_request(username, repos, state='open'):
    url = 'https://api.github.com/repos/{}/{}/pulls?state={}'.format(username, repos, state)
    response = requests.get(url, headers=get_headers())
    return response.json()


def get_user_commits(url):
    response = requests.get('{}/commits'.format(url), headers=get_headers())
    resp = response.json()
    res = []
    for j in resp:
        dict_1 = j.get('commit')
        mes = dict_1.get('message')
        res.append(mes)
    return res


def check_prefix(title):
    errors = []
    if title is None:
        return notice_1
    lst = title.split(' ')
    if len(lst) < 2:
        return notice_2
    lst_1 = lst[0].split('-')
    if lst[1] not in words_of_action:
        errors.append(notice_7)
    if len(lst_1) < 2:
        errors.append(notice_3)
    else:
        if lst_1[0] not in project_names:
            if lst_1[0].upper() not in project_names:
                errors.append(notice_4)
            else:
                errors.append(notice_5)
        if lst_1[1] not in numbers_of_group:
            errors.append(notice_6)
    result = ''
    for i in errors:
        result = result+i
    return result


def check_requests(username, repos, state='open'):
    pulls = get_user_pull_request(username, repos, state='open')
    fin = []
    for i in pulls:
        title = i.get('title')
        title_errors = check_prefix(title)
        if title_errors == '':
            title_errors = notice
        res = 'Title: {}\nVerify_Result: {}'.format(title, title_errors)
        fin.append(res)
    return fin

def send_check_result(pull, comment):
    if len(comment) > 0:
        r = requests.post(pull['url']+'/comments', headers=get_headers(), data=json.dumps(check_requests(pull, comment)).encode('utf8'))


def maximum_date(lst, num, num_1, piece_1, piece_2, spliter):
    lst_2 = []
    for i in lst:
        i = i.split('T')
        lst_1 = i[num].split(spliter)
        lst_2.append(int(lst_1[num_1]))
    res = []
    for i in lst:
        if int(i[piece_1:piece_2]) == max(lst_2):
            res.append(i)
    return res


def last_comment_on_pull(url):
    response = requests.get('{}/comments'.format(url), headers=get_headers())
    resp = response.json()
    dates = []
    for j in resp:
        date = j.get('created_at')
        dates.append(date)
    return last_note(dates)


def last_note(lst_1):
    lst = []
    for i in lst_1:
        lst.append(i[0:19])
    max_years = maximum_date(lst, 0, 0, 0, 4, '-')
    max_months = maximum_date(max_years, 0, 1, 5, 7, '-')
    max_day = maximum_date(max_months, 0, 2, 8, 10, '-')
    max_hour = maximum_date(max_day, 1, 0, 11, 13, ':')
    max_min = maximum_date(max_hour, 1, 1, 14, 16, ':')
    max_sec = maximum_date(max_min, 1, 2, 17, 19, ':')
    return max_sec[0]


def check_commits(username, repos, state='open'):
    pulls = get_user_pull_request(username, repos, state='open')
    for i in pulls:
        j = i.get('url')
        response = requests.get('{}/commits'.format(j), headers=get_headers())
        resp = response.json()
        dates = []
        for i in resp:
            dict_1 = i.get('commit')
            dict_2 = dict_1.get('author')
            date = dict_2.get('date')
            dates.append(date)
        last_comment = last_comment_on_pull(j)
        last_commit = last_note(dates)
        lst = [last_comment, last_commit]
        if last_commit == last_note(lst):
            verify_result(last_commit)
