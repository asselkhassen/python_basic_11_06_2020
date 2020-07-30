""" Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

file = open('test_task_2.txt', 'r', encoding='UTF-8')
lines = file.readlines()

print('Колчество строк: ', len(lines))

number = 1
for line in lines:
    print(f'Количество слов в строке № {number}', len(line.split(sep=' ')))
    number += 1


