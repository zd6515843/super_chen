def build_info00(firstName, lastName, **userInfo):
    info = {}
    info['FirstName'] = firstName
    info['LastName'] = lastName
    for key, value in userInfo.items():
        info[key] = value
    return info


def build_info(firstName, lastName, **userInfo):
    info = {}
    info['FirstName'] = firstName
    info['LastName'] = lastName
    for key, value in userInfo.items():
        info[key] = value
    return info


def build_info22(firstName, lastName, **userInfo):
    info = {}
    info['FirstName'] = firstName
    info['LastName'] = lastName
    for key, value in userInfo.items():
        info[key] = value
    return info


def function_long(
        parameter1, parameter2, parameter3,
        parameter4, parameter5, parameter6):
    print('6666')
