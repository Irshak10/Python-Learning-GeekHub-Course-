# 1. Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
#   Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
#   Логіка наступна:
#       якщо введено коректну пару ім'я/пароль - вертається <True>;
#       якщо введено неправильну пару ім'я/пароль і <silent> == <True> - функція вертає <False>, інакше (<silent> == <False>) - породжується виключення LoginException


# Моя відповідь:

class LoginException(Exception):
	pass


def users(username, password, silent = False):
	dic = {'Roma': '123qwerty', 'Maks': 'fsedwtet', 'Dima': 'sdfs4','Egor':'324234234','Slava':'fdgdfg79'}

	try:

		if password == dic.get(username):
			silent = True
			print(f'Здравствуйте {username}')

		elif password != dic.get(username) and silent == True:
			return False
		
		else:
			raise LoginException
	except LoginException:
		print('Данні не вірні')


users('Roma', '123qwerty')