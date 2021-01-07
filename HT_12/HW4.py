# -*- coding: utf-8 -*-

# 4. Створіть клас в якому буде атребут, який буде рахувати кількість створених екземплярів класів.

# Моя відповідь: 

class People(object):
	"""Клас People"""
	number_of_people = 0

	def __init__(self, name):
		self.name = name
		People.number_of_people += 1

man1 = People('Roma')
print(People.number_of_people)

man2 = People('Max')
print(People.number_of_people)

man3 = People('Alex')
print(People.number_of_people)