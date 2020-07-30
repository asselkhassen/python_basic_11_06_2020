""" Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""


file = open('test_task_1.txt', 'w', encoding='UTF-8')

while True:
    data = input('Введите данные: ')
    if data == '':
        break
    else:
        file.write(data + '\n')

file.close()

