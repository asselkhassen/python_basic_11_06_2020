""" Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from random import random

file = open('test_task_5.txt', 'w', encoding='UTF-8')

for number in range(0, 20):
    num = int(random() * 1000)
    file.write(f'{num} ')

file.close()

file_2 = open('test_task_5.txt', 'r', encoding='UTF-8')

numbers = file_2.readline().split(' ')
sum_numbers = 0

for n in numbers:
    try:
        sum_numbers += int(n)
    except ValueError:
        continue

print(sum_numbers)

