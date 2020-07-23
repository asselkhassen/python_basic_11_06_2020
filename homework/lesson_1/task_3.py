"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369
"""

n = int(input('Введите число n'))
calculation = n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n))
print(calculation)
