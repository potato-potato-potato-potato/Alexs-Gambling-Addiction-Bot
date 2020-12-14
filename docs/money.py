import json


def get_money(file, username):
    userdata = __find_user(file, username)
    if not userdata:
        return

    return userdata['money']


def add_money(file, username):
    """
    userdata = __find_user(file, username)
    if not userdata:
        return
    :param file:
    :param username:
    :return:
    """

    __add_user(file, username)


def __add_user(file, username):
    data = {}

    with open(file, 'r') as json_file:
        temp_data = json.load(json_file)
        data['users'] = temp_data['users']

    data['users'].append({
        'name': username,
        'money': 0
    })
    with open(file, 'w') as outfile:
        json.dump(data, outfile)


def __find_user(file, username):
    with open(file, 'r') as json_file:
        data = json.load(json_file)
        for user in data['users']:
            if user['name'] == username:
                return user
    return None