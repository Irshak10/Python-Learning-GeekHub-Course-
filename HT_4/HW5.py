# 5. Запишіть в один рядок генератор списку (числа в діапазоні від 0 до 100), сума цифр кожного елемент якого буде дорівнювати 10.
#   Перевірка: [19, 28, 37, 46, 55, 64, 73, 82, 91]


# Моя відповідь:

generator = [int(str(i) + str(n)) for i in range(100) for n in range (100) if i + n == 10 and i != 10 and n != 10 ]

print(generator)

