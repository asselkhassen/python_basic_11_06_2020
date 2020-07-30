""" Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

file_eng = open('test_task_4_eng.txt', 'r', encoding='UTF-8')
file_rus = open('test_task_4_rus.txt', 'w', encoding='UTF-8')

file_eng_lines = file_eng.readlines()

translate_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}

for eng_line in file_eng_lines:
    my_list = eng_line.split(sep=' ')
    file_rus.write(eng_line.replace(my_list[0], translate_dict[my_list[0]]))

file_rus.close()



