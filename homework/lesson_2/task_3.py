"""Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
"""
month = 0
while True:
    month = input('Введите месяц: ')
    if month.isdigit():
        month = int(month)
        if 1 <= month <= 12:
            break
    print('Введите целое число от 1 до 12')

winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

dict = {
    'Зима': winter,
    'Весна': spring,
    'Лето': summer,
    'Осень': autumn
}

for key in dict:
    if month in dict[key]:
        print(key)
        break