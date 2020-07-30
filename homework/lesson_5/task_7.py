""" Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import json

file = open('test_task_7.txt', 'r', encoding='UTF-8')
file_lines = file.readlines()

my_list = []
profits = {}
average_profit = {}
avg_profit_sum = 0
counter = 0

for line in file_lines:
    company_info = line.split(' ')
    profit = int(company_info[2]) - int(company_info[3])
    profits.update({company_info[0]: profit})
    if profit > 0:
        avg_profit_sum += profit
        counter += 1

average_profit.update({'average_profit': int(avg_profit_sum / counter)})
my_list.append(profits)
my_list.append(average_profit)

json_file = open("test_task_7.json", "w")
json.dump(my_list, json_file)
json_file.close()
