""" Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""


my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
duplicate_list = []
new_list = []

for idx, element in enumerate(my_list):
    add_to_list = True
    if element in duplicate_list:
        continue
    for index in range(idx + 1, len(my_list)):
        if element == my_list[index]:
            duplicate_list.append(element)
            add_to_list = False
            break

    if add_to_list:
        new_list.append(element)

print(new_list)

