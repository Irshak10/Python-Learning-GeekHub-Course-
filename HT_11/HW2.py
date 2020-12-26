# -*- coding: utf-8 -*-

# 2. Створити клас Person, в якому буде присутнім метод __init__ який буде приймати * аргументів, які зберігатиме в відповідні змінні. Методи, які повинні бути в класі Person - show_age, print_name, show_all_information.
#    - Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атребут profession.

# Моя відповідь: 

class Person(object):
    """Клас Person, в якому присутнім метод __init__ який приймає * аргументів, які зберігатиме в відповідні змінні. Методи, які присутні класі Person: show_age, print_name, show_all_information."""
    def __init__(self, *arg):
        self.age = arg[0]
        self.name = arg[1]
        self.profession = None

    def show_age(self):
        return self.age

    
    def print_name(self):
        return self.name


    def show_all_information(self):
        return f'Вік: {self.age}, імя: {self.name}, професія: {self.profession}'


a = Person(24, 'Roma')
a.profession = 'QA Engineer'
print(a.show_age())
print(a.print_name())
print(a.show_all_information())
print()

b = Person(25, 'Alex')
b.profession = 'Developer'
print(b.show_age())
print(b.print_name())
print(b.show_all_information())
print()

print(Person.__doc__)