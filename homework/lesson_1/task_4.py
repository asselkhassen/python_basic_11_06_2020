"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

number = int(input('Введите число'))
array = [int(x) for x in str(number)]

index = 0
max = array[0]
while index < len(array):
    if max < array[index]:
        max = array[index]
    index += 1
print('Самая большая цифра в числе:', max)