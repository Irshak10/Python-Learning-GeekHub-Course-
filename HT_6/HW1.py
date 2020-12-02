# Домашнє завдання №6 (термін виконання - до наступної середи, 02.12.2020):
# Доповніть програму-банкомат з попереднього завдання таким функціоналом, як використання банкнот. 
# Отже, у банкомата повинен бути такий режим як "інкассація", за допомогою якого в нього можна "загрузити" деяку кількість банкнот (вибирається номінал і кількість). 
# Зняття грошей з банкомату повинно відбуватись в межах наявних банкнот за наступним алгоритмом - видається мінімальна кількість банкнот наявного номіналу. 
# P.S. Будьте обережні з використанням "жадібного" алгоритму (коли вибирається спочатку найбільша банкнота, а потім - наступна за розміром і т.д.) - в деяких випадках він працює неправильно або не працює взагалі. Наприклад, якщо треба видати 160 грн., а в наявності є банкноти номіналом 20, 50, 100, 500,  банкомат не зможе видати суму (бо спробує видати 100 + 50 + (невідомо), а потрібно було 100 + 20 + 20 + 20 )

# Моя відповідь: 
import json


#
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
			if user_id == '8':
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
					transactions = json.dump(f'User added {inc_sum * n_sum} UAH - Amount {n_sum} banknotes on {inc_sum} UAH | ',f)
				print(f'Ваш баланс поповнено на {inc_sum * n_sum} UAH\nВнеcено {n_sum} банкнот по {inc_sum} UAH\n')
				prestart_menu()
				choose_number = str(start())    
			else:
				plus_sum = int(input('Введіть суму поповнення: '))
				user_balance = int(user_balance) + plus_sum
				with open(f'balance{user_id}.json', 'w') as f:
					user_balance = json.dump(user_balance,f)
				with open(f'{user_id}_transactions.data.json', 'a') as f:
					transactions = json.dump(f'User added {plus_sum} UAH | ',f)
				print(f'Ваш баланс поповнено на {plus_sum} UAH\n')      
				prestart_menu()
				choose_number = str(start())
		elif (choose_number == '3'):
			with open(f'balance{user_id}.json', 'r') as f:
				user_balance = json.load(f)
			
			minus_sum = int(input('Введіть суму, яку бажаєте вивести: '))
			collection(minus_sum)

			if minus_sum > user_balance:
				print('Недостатньо коштів для виводу')
			else:
				user_balance = int(user_balance) - minus_sum
				with open(f'balance{user_id}.json', 'w') as f:
					user_balance = json.dump(user_balance,f)
			with open(f'{user_id}_transactions.data.json', 'a') as f:
				transactions = json.dump(f'User removed {minus_sum} UAH | ',f)
			print(f'З балансу знято {minus_sum} UAH\n')    
			prestart_menu()
			choose_number = str(start())
		else:
			print('Обрана невідома команда, повторіть введення')
			prestart_menu()
			choose_number = str(start())
	print('Вихід з програми')        


# Виклик основної функції із значеннями, які повернулись з функції validat()
check_user = validat()
if check_user:
	choose_number, user_id = check_user
	workflow(choose_number, user_id)
	

# def collection(minus_sum):
# 	with open(f'balance8.json', 'r') as f:
# 		user_balance_inc = json.load(f)
	
# 	for o in user_balance_inc['nominals']:
# 		if minus_sum == 
# in progress...




