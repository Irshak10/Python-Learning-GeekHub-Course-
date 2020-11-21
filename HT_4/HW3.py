# 3. На основі попередньої функції створити наступний кусок кода:
#   а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
#   б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
#      Name: vasya
#      Password: wasd
#      Status: password must have at least one digit
#      -----
#      Name: vasya
#      Password: vasyapupkin2000
#      Status: OK
#   P.S. Не забудьте використати блок try/except ;)

# Моя відповідь:


class MyError(Exception):
    pass


def users(username, password):
    try:
        if len(username) < 3 or len(username) > 50:
            raise MyError(len(username))

    except MyError:
        return 'wasd'
    else:
        return 'ОК'


    try:
        if len(password) < 8:
            raise MyError(len(password))
        elif not any([i.isdigit() for i in password]):
            raise MyError(password)
        elif not any([i.isupper() for i in password]):
            raise MyError(password)
        
    except MyError:
        return 'Пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру і одну букву'
    else:
        return f'Ваш пароль {password} підходящий для реєстрації'

variants = [['123sdgs', 'bbbbbBb1b'],['12', 'bbbb'],['12', 'bbbbbBbb'],['123', 'bbbbb11111']]

for i in variants:
	print(f'Name:{i[0]}')
	print(f'Password:{i[1]}')
	print(f'Status:{users(*i)}\n-----')
