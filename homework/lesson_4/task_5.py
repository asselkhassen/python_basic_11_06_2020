""" Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка. Подсказка: использовать функцию reduce().
"""


from functools import reduce


def multiply_func(element_prev, element):
    return element_prev * element


new_list = [element for element in range(100, 1001) if element % 2 == 0]
result = reduce(multiply_func, new_list)

print('Список: ', new_list)
print('Результат: ', result)



