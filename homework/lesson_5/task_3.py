""" Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

file = open('test_task_3.txt', 'w', encoding='UTF-8')

salaries = {
    'Картоев': 12000,
    'Сысоев': 10000,
    'Малюгин': 15000,
    'Иванов': 20000,
    'Петров': 30000,
    'Степанов': 40000,
    'Дмитриев': 50000
}

total = 0
for name, salary in salaries.items():
    file.write(f'{name}: {salary} \n')
    if salary < 20000:
        print(f'{name}')
    total += salary
print('Средняя величина дохода сотрудников: ', total / len(salaries))