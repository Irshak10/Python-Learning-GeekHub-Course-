# -*- coding: utf-8 -*-

# 2. Видозмініть програму так, щоб метод __init__ мався в класі «геометричні фігури» та приймав кольор фігури при створенні екземпляру, 
# а методи __init__ підкласів доповнювали його та додавали початкові розміри.

# Моя відповідь: 

class Figure(object):
	"""Батьківський клас з методом зміни кольору"""
	def __init__(self, color='white'):
		self.color = color

	def change_color(self, new_color):
		self.color = new_color

	
class Oval(Figure):
	""" Дочірній клас oval, який унаслідував всі данні від класу figure """
	def __init__(self, radius, width, height, color='pink'):
		super(Oval, self).__init__(color)
		self.radius = radius
		self.width = width
		self.height = height

	def info_values_oval(self):
		return f'{self.color}, {self.radius}, {self.width}, {self.height}'
			

class Square(Figure):
	""" Ще один дочірній клас square, який також унаслідував всі данні від класу figure """
	def __init__(self, a, b, color='grey'):
		super(Square, self).__init__(color)
		self.a = a
		self.b = b

	def info_values_square(self):
		return f'{self.color}, {self.a}, {self.b}'

a = Figure()
print(a.color)
a.change_color('black')
print(a.color)

b = Oval(10, 3, 4)
print(b.info_values_oval())
b.change_color('yellow')
print(b.color)

c = Square(5, 4)
print(c.info_values_square())
c.change_color('red')
print(c.color)