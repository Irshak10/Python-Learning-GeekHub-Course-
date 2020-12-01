# 1. Програма-банкомат.
#    Створити програму з наступним функціоналом:
#       - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.data>);
#       - кожен з користувачів має свій поточний баланс (файл <{username}_balance.data>) та історію транзакцій (файл <{username}_transactions.data>);
#       - є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених даних (введено число; знімається не більше, ніж є на рахунку).
#    Особливості реалізації:
#       - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
#       - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
#       - файл з користувачами: тільки читається. Якщо захочете реалізувати функціонал додавання нового користувача - не стримуйте себе :)
#    Особливості функціонала:
#       - за кожен функціонал відповідає окрема функція;
#       - основна функція - <start()> - буде в собі містити весь workflow банкомата:
#       - спочатку - логін користувача - програма запитує ім'я/пароль. Якщо вони неправильні - вивести повідомлення про це і закінчити роботу (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на ентузіазмі :) )
#       - потім - елементарне меню типа:
#         Введіть дію:
#            1. Продивитись баланс
#            2. Поповнити баланс
#            3. Вихід
#       - далі - фантазія і креатив :)


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