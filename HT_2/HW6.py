#6. Маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" -> просто потицяв по клавi
#   Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
#-  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
#-  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
#-  якщо довжина бульше 50 - > ваша фантазiя

# Моя відповідь:

def clever_fun(a):
	
	b = len(a)
	count_num = 0
	count_letter = 0
	sum_num = 0
	only_letter_str = str()
	symbols = 0

	for i in a:
		if i.isdigit():
			count_num += 1
			sum_num += int(i)
		elif i.isalpha():
			count_letter += 1
			only_letter_str += i
		else:
			symbols += 1

	if b >= 30 and b <= 50:
		print(f'{b} - довжина строки')
		print(f'{count_letter} - кількість букв')
		print(f'{count_num} - кількість цифр')
	elif b < 30:
		print(f'{sum_num} - сума цифр')
		print(only_letter_str + ' - це строка, яка складається виключно із букв')
	else:
		print(str(symbols) + '% - рівень моєї фантазiї :)') 	
	return


clever_fun('seghsdh423hdfhdfhdf$^#^GSDG@#%^^^^dk46k46kdh12353(*@')