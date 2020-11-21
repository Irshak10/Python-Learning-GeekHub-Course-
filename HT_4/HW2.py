# 2. Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
#   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
#   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
#   - щось своє (пароль повинен мати хоча б одну букву у верхньому регистрі)
#   Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.


# Моя відповідь:


class MyError(Exception):
    pass


def users(username, password):
    try:
        if len(username) < 3 or len(username) > 50:
            raise MyError(len(username))

    except MyError:
        print('Імя повинно бути не меншим за 3 символа і не більшим за 50')
    else:
        print(f'Вітаю {username}')


    try:
        if len(password) < 8:
            raise MyError(len(password))
        elif not any([i.isdigit() for i in password]):
            raise MyError(password)
        elif not any([i.isupper() for i in password]):
            raise MyError(password)
        
    except MyError:
        print('Пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру і одну букву')
    else:
        print(f'Ваш пароль {password} підходящий для реєстрації')


users('123', 'bbbbbBb1b')