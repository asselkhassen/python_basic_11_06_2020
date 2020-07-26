""" Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""


def collect_user_info(**kwargs):
    info = ''
    for key, value in kwargs.items():
       info += f'{key}: {value}, '
    print(info)

user_info = {
    'name': 'Assel',
    'surname': 'Khassen',
    'year': 1996,
    'city': 'Nur-Sultan',
    'email': 'aselkhasen@gmail.com',
    'phone': '8(777)777-77-77'
}
collect_user_info(**user_info)

