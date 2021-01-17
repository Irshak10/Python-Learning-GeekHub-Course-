# HT #13 - термін виконання - 20.01.2021 (наступна середа).
#Перепишіть програму-банкомат на використання бази даних для збереження всих даних. Використовувати БД sqlite3 та натівний Python.

# Моя відповідь: 
import json
import random
import sqlite3

def prestart_menu():
	print('Введіть відповідну цифру для вибору операції: 1 - (Перевірка балансу), 2 - (Поповнення рахунку), 3 - (Вивод коштів) 4 - (Вихід)')

def start():
	choose_number = str(input('Ваша дія: '))
	return choose_number

# Валідація користувача по логіну та паролю і присвоєння користувачу відповідного id.
def validat():

	# users_data = [
	# 		(1,'Roman','Qwerty12345',' '),
	# 		(2,'Valeriy','Qwerty123',' '),
	# 		(3,'Liudmila','Qwerty1234',' '),
	# 		(4,'Irina','Qwerty123456',' ''),
	# 		(5,'Olya','Qwerty11313',' '),
	# 		(6,'Natalia','Qwerty12316717',' '),
	# 		(7,'Andriy','Qwerty67967',' '),
	# 		(8,'Alex','Qwerty15151', ' '),
	# 		(9,'Diana','Qwe121rty', ' '),
	# 		(10,'Dmitriy','Qwe12312rty',' '),
	# 		(11,'Inc','Inc',' ')
	# 	]

	with sqlite3.connect('bankomat.db') as db:
		cursor = db.cursor()
		cursor.execute("""CREATE TABLE IF NOT EXISTS users_data (
			id INTEGER,
			login TEXT,
			password TEXT,
			transactions_user TEXT
						)""")
			
		# cursor.executemany("""INSERT INTO users_data VALUES(?, ?, ?, ?)""",users_data)
		
		


	login = str(input('Введіть Ваш логін (імя, латиницею): '))
	password = str(input('Введіть Ваш пароль: '))
	with sqlite3.connect('bankomat.db') as db:
		cursor = db.cursor()
		data = cursor.execute(f"SELECT * from users_data WHERE login = '{login}' and password = '{password}'")
		
		for i in data:
			if login == i[1] and password == i[2]:
				user_id = i[0]
				print('Вказані данні - вірні')
				prestart_menu()
				choose_number = str(start())
				return (choose_number, user_id)
			elif login == i[1] and password != i[2]:
				print('Пароль вказаний не вірно')
				continue
			elif login != i[1] and password == i[2]:
				print('Логін вказаний не вірно')
				continue
			elif login != i[1] and password != i[2]:
				continue
	print("Данні не вірні, вихід із системи")   
      
# Словник доступних банкнот
def inc_balance():
	with open(f'balance11.json', 'r') as f:
		banknote = json.load(f)
	dic = {}
	for i in banknote['nominals']:
		dic[int(i['inc_sum'])] = int(i['n_sum'])
	return dic

# Реалізація виводу коштів згідно з доступними банкнотами
def withdraw(user_sum, banknote_data):
	finaly_sum = []
	sort_nominals = sorted(inc_balance(), reverse=True)

	while sum(finaly_sum) < user_sum:
		next_iter = False
		for i in sort_nominals:
			if next_iter:
				break

			elif i + sum(finaly_sum) <= user_sum:
				for k in sort_nominals:
					if (user_sum - sum(finaly_sum) - i) % k == 0:
						finaly_sum.append(i)
						next_iter = True
						break

		if not finaly_sum:
			print('Банкомат немає змоги видати вказану суму доступнимим купюрами')
			break 

	return finaly_sum

#Доступний workflow банкомата (Основна логіка програми): 
def workflow(choose_number, user_id): 
	while choose_number != '4':
		if (choose_number == '1'):
			if user_id == 11:
				with open(f'balance{user_id}.json', 'r') as f:
					user_balance = json.load(f)
				print(f'Ваш баланс: {user_balance}\n')
				prestart_menu()
				choose_number = str(start())
			else:
				with sqlite3.connect('bankomat.db') as db:
					cursor = db.cursor()
					user_balance = cursor.execute(f"SELECT money FROM balance WHERE id = '{user_id}'")
				print(f'Ваш баланс: {user_balance.fetchone()[0]}\n')
				prestart_menu()
				choose_number = (start())
		elif (choose_number == '2'):
			with sqlite3.connect('bankomat.db') as db:
					cursor = db.cursor()
					user_balance = cursor.execute(f"SELECT money FROM balance WHERE id = '{user_id}'")
					
			if user_id == 11:
				inc_sum = int(input('Введіть номінал поповнення: '))
				n_sum = int(input('Введіть кількість банкнот: '))
				for y in user_balance['nominals']:
					if inc_sum == int(y['inc_sum']):
						y['n_sum'] = str(int(y['n_sum']) + n_sum)
						break
				else:
					user_balance['nominals'].append({'inc_sum': str(inc_sum), 'n_sum': str(n_sum)})
				with open(f'balance{user_id}.json', 'w') as f:
					json.dump(user_balance,f)
				
				save = f'INC added {inc_sum * n_sum} UAH - Amount {n_sum} banknotes on {inc_sum} UAH | '
				with sqlite3.connect('bankomat.db') as db:
					cursor = db.cursor()
					cursor.execute(f"UPDATE users_data SET transactions_user = transactions_user ||'{save}' WHERE id = '{user_id}'")
					
		
				print(f'Баланс Банкомату поповнено на {inc_sum * n_sum} UAH\nІнкасацією внеcено {n_sum} банкнот по {inc_sum} UAH\n')
				prestart_menu()
				choose_number = str(start())  
			else:		
				plus_sum = int(input('Введіть суму поповнення: '))
				user_balance = int(user_balance.fetchone()[0]) + plus_sum
				save1 = f'User added {plus_sum} UAH | '
				with sqlite3.connect('bankomat.db') as db:
					cursor = db.cursor()
					cursor.execute(f"UPDATE users_data SET transactions_user = transactions_user ||'{save1}' WHERE id = '{user_id}'")
					

				with sqlite3.connect('bankomat.db') as db:
					cursor = db.cursor()
					cursor.execute(f"UPDATE balance SET money = '{user_balance}' WHERE id = '{user_id}'")
					
				# with open(f'balance{user_id}.json', 'w') as f:
				# 	json.dump(user_balance,f)
				print(f'Ваш баланс поповнено на {plus_sum} UAH\n')      
				prestart_menu()
				choose_number = str(start())
		elif (choose_number == '3'):
			possible = True
			with sqlite3.connect('bankomat.db') as db:
					cursor = db.cursor()
					user_balance = cursor.execute(f"SELECT money FROM balance WHERE id = '{user_id}'")
					user_balance = user_balance.fetchone()[0]
						
			if user_id == 11:
				print('Вивід коштів для інкасації недоступний')
				choose_number = str(start())
				possible = False

			else:	
				minus_sum = int(input('Введіть суму, яку бажаєте вивести: '))
				if minus_sum > int(user_balance):
					print('Недостатньо коштів для виводу')
					possible = False

				else:
					with open(f'balance11.json', 'r') as f:
						inc_balance11 = json.load(f)
					for o in inc_balance11['nominals']:
						for y in withdraw(minus_sum, inc_balance()):
							if y == int(o['inc_sum']):
								o['n_sum'] = str(int(o['n_sum']) - 1)
								
								if int(o['n_sum']) < 0:
									o['n_sum'] = '0'
									print('Банкомат немає змоги видати вказану суму доступнимим купюрами')
									possible = False
								break
			if possible:		
				user_balance = int(user_balance) - minus_sum
				with open(f'balance11.json', 'w') as f:
					json.dump(inc_balance11,f)
				with sqlite3.connect('bankomat.db') as db:
					cursor = db.cursor()
					cursor.execute(f"UPDATE balance SET money = '{user_balance}' WHERE id = '{user_id}'")	
				
				save2 = f'User removed for balance {minus_sum} UAH | '
				with sqlite3.connect('bankomat.db') as db:
					cursor = db.cursor()
					cursor.execute(f"UPDATE users_data SET transactions_user = transactions_user ||'{save2}' WHERE id = '{user_id}'")
					
				print(f'З балансу знято {minus_sum} UAH, Вам видано {withdraw(minus_sum, inc_balance())}\n')		
			prestart_menu()
			choose_number = str(start())
		else:
			print('Обрана невідома команда, повторіть введення')
			prestart_menu()
			choose_number = str(start())
	print('Вихід з програми')        

# Виклик функції із значеннями, які повернулись з функції validat()
check_user = validat()
if check_user:
	choose_number, user_id = check_user
	workflow(choose_number, user_id)
