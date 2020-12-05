# Домашнє завдання №6 (термін виконання - до наступної середи, 02.12.2020):
# Доповніть програму-банкомат з попереднього завдання таким функціоналом, як використання банкнот. 
# Отже, у банкомата повинен бути такий режим як "інкассація", за допомогою якого в нього можна "загрузити" деяку кількість банкнот (вибирається номінал і кількість). 
# Зняття грошей з банкомату повинно відбуватись в межах наявних банкнот за наступним алгоритмом - видається мінімальна кількість банкнот наявного номіналу. 
# P.S. Будьте обережні з використанням "жадібного" алгоритму (коли вибирається спочатку найбільша банкнота, а потім - наступна за розміром і т.д.) - в деяких випадках він працює неправильно або не працює взагалі. Наприклад, якщо треба видати 160 грн., а в наявності є банкноти номіналом 20, 50, 100, 500,  банкомат не зможе видати суму (бо спробує видати 100 + 50 + (невідомо), а потрібно було 100 + 20 + 20 + 20 )

# Моя відповідь: 
import json


def prestart_menu():
	print('Введіть відповідну цифру для вибору операції: 1 - (Перевірка балансу), 2 - (Поповнення рахунку), 3 - (Вивод коштів) 4 - (Вихід)')

def start():
	choose_number = str(input('Ваша дія: '))
	return choose_number

# Валідація користувача по логіну та паролю (зчитування данних з json файлу) і присвоєння користувачу відповідного id.
def validat():
	login = str(input('Введіть Ваш логін (імя, латиницею): '))
	password = str(input('Введіть Ваш пароль: '))
	with open('users_data.json', 'r') as f:
		data = json.load(f)
	for i in data['users']:
		if login == i['firstName'] and password == i['password']:
			user_id = i['id']
			print('Вказані данні - вірні')
			prestart_menu()
			choose_number = str(start())
			return (choose_number, user_id)
		elif login == i['firstName'] and password != i['password']:
			print('Пароль вказаний не вірно')
			continue
		elif login != i['firstName'] and password == i['password']:
			print('Логін вказаний не вірно')
			continue
		elif login != i['firstName'] and password != i['password']:
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
			with open(f'balance{user_id}.json', 'r') as f:
				user_balance = json.load(f)
			print(f'Ваш баланс: {user_balance}\n')
			prestart_menu()
			choose_number = str(start())
		elif (choose_number == '2'):
			with open(f'balance{user_id}.json', 'r') as f:
				user_balance = json.load(f)
			if user_id == '11':
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

				with open(f'{user_id}_transactions.data.json', 'a') as f:
					json.dump(f'User added {inc_sum * n_sum} UAH - Amount {n_sum} banknotes on {inc_sum} UAH | ',f)
				print(f'Баланс Банкомату поповнено на {inc_sum * n_sum} UAH\nІнкасацією внеcено {n_sum} банкнот по {inc_sum} UAH\n')
				prestart_menu()
				choose_number = str(start())    
			else:
				plus_sum = int(input('Введіть суму поповнення: '))
				user_balance = int(user_balance) + plus_sum
				with open(f'balance{user_id}.json', 'w') as f:
					json.dump(user_balance,f)
				with open(f'{user_id}_transactions.data.json', 'a') as f:
					json.dump(f'User added {plus_sum} UAH | ',f)
				print(f'Ваш баланс поповнено на {plus_sum} UAH\n')      
				prestart_menu()
				choose_number = str(start())
		elif (choose_number == '3'):
			possible = True
			with open(f'balance{user_id}.json', 'r') as f:
				user_balance = json.load(f)
			if user_id == '11':
				print('Вивід коштів для інкасації недоступний')
			else:	
				minus_sum = int(input('Введіть суму, яку бажаєте вивести: '))
				if minus_sum > user_balance:
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
				with open(f'balance{user_id}.json', 'w') as f:
						json.dump(user_balance,f)	
				with open(f'{user_id}_transactions.data.json', 'a') as f:
					json.dump(f'User removed {minus_sum} UAH | ',f) 
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
