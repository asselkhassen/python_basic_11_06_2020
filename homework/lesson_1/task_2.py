"""
Пользователь вводит время в секундах. Переведите время в часы,
минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк
"""

time_in_sec = int(input('Введите время в секундах'))
hours = time_in_sec // 3600
minutes = (time_in_sec - hours * 3600) // 60
seconds = time_in_sec - (hours * 3600 + minutes * 60)
print(f'Время: {hours}:{minutes}:{seconds}')