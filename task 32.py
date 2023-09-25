# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше
# заданного максимума)
import random

progression = [random.randint(1, 100) for i in range(10)]
print("Массив:", progression)
min_value = int(input("Введите минимальное значение: "))
max_value = int(input("Введите максимальное значение: "))

indexes = []

for i in range(len(progression)):
    if min_value <= progression[i] <= max_value:
        indexes.append(i)

print("Индексы элементов, принадлежащих заданному диапазону:", indexes)