# 2. Користувачем вводиться початковий і кінцевий рік. Створити цикл, який виведе всі високосні роки в цьому проміжку (границі включно).

# Моя відповідь:

start_year = int(input())
final_year = int(input())

for i in range(start_year, final_year+1):
	if i % 400 == 0 or (i % 4 == 0 and i % 100 != 0):
		print(i)