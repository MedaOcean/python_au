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
