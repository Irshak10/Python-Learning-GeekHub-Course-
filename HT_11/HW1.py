# -*- coding: utf-8 -*-

# 1. Створити клас Calc, який буде мати атребут last_result та 4 методи. Методи повинні виконувати математичні операції з 2-ма числами, а саме додавання, віднімання, множення, ділення.
#    - Якщо під час створення екземпляру класу звернутися до атребута last_result він повинен повернути пусте значення
#    - Якщо використати один з методів - last_result повенен повернути результат виконання попереднього методу.
#    - Додати документування в клас (можете почитати цю статтю: https://realpython.com/documenting-python-code/ )

# Моя відповідь: 

class Calc(object):
	"""Клас Calc, який має атребут last_result та 4 методи які оперують 2-ма числами: додавання, віднімання, множення, ділення (в наявності помилка при діленні на нуль). Реалізована можливість виведення результату виконання попереднього методу з допомогою атрибуту last_result. При зверненні до атребута last_result, під час створення екземпляру класу, видається пусте значення (None)"""
	
	last_result = None # Атрибут, який зберігає результат останньої виконаної операції

	def sum_1(self, a, b):  
		"""Метод 1: додавання двох чисел"""
		result = a + b
		self.last_result = result
		return result

		
	def subtraction_1(self, a, b):
		"""Метод 2: віднімання двох чисел"""
		last_result = a - b
		self.last_result = result
		return result

		
	def multiplication_1(self, a, b): 
		"""Метод 3: множення двох чисел"""
		result = a * b
		self.last_result = result
		return result


	def division_1(self, a, b): 
		"""Метод 4: ділення двох чисел (в наявності помилка при діленні на нуль)"""
		if b == 0:
			return "На нуль ділити не можна"
		else:
			result = a / b
			self.last_result = result
			return result
	

x = Calc() # Об'єкт

print(x.sum_1(6,2))
print(x.last_result)
print(x.division_1(6,3))
print(x.last_result)

print(Calc.__doc__)