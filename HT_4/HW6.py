# 6. Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
#   P.S. Повинен вертатись генератор.
#   P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range


# Моя відповідь:

class Error(Exception):
	pass
		

def custom_range(*args):
	if len(args) == 1:
		start = 0
		finish = args[0]
		step = 1

	elif len(args) == 2:
		start = args[0]
		finish = args[1]
		step = 1
	elif len(args) == 3:
		start = args[0]
		finish = args[1]
		step = args[2]
	else:
		raise Error

	i = start
	if step > 0:

		while i < finish:
			yield i 
			i += step
			
	elif step < 0:
		while i > finish:
			yield i 
			i += step
			
	else:
		raise Error


print(list(custom_range(0, 5, 1)))
