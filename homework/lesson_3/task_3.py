""" Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(arg_1, arg_2, arg_3):
    args = sorted([arg_1, arg_2, arg_3], reverse=True)
    return args[0] + args[1]


print(my_func(11, 949, 843))