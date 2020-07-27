""" Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
"""

from itertools import cycle, count


for number in count(1, 2):
    print(number)
    if number == 303:
        break

my_list = [1, 2, 3, 5, 6, 7, 'alskdjf', 'lajsdofji']

cycle_counter = 0
for element in cycle(my_list):
    print(element)
    if element == 'lajsdofji':
        cycle_counter += 1
    if cycle_counter == 3:
        break
