""" Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с
одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них
"""

rating_list = [15, 12, 9, 7, 7]
user_rating = 0
while True:
    user_rating = input('Введите элемент рейтинга: ')
    if user_rating.isdigit():
        user_rating = int(user_rating)
        break
    print('Элемент должен быть числом')

for i in range(0, len(rating_list)):
    if i == 0 and user_rating >= rating_list[i]:
        rating_list.insert(i, user_rating)
        break
    elif i > 0 and rating_list[i - 1] >= user_rating >= rating_list[i]:
        rating_list.insert(i, user_rating)
        break
    elif i == len(rating_list) - 1 and user_rating <= rating_list[i]:
        rating_list.append(user_rating)

print(rating_list)