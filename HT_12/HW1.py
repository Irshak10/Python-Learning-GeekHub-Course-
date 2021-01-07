# -*- coding: utf-8 -*-

# 1. Напишіть програму, де клас «геометричні фігури» (figure) містить властивість color з початковим значенням white і метод для зміни кольору фігури, 
# а його підкласи «овал» (oval) і «квадрат» (square) містять методи __init__ для завдання початкових розмірів об'єктів при їх створенні.

# Моя відповідь: 

class Figure(object):
	"""Батьківський клас з методом зміни кольору"""
	color = 'white'

	def change_color(self, new_color):
		self.color = new_color

	
class Oval(Figure):
	""" Дочірній клас oval, який унаслідував всі данні від класу figure """
	def __init__(self, radius, width, height):
		super(Oval, self).__init__()
		self.radius = radius
		self.width = width
		self.height = height

	def info_values_oval(self):
		return f'{self.radius}, {self.width}, {self.height}'
			

class Square(Figure):
	""" Ще один дочірній клас square, який також унаслідував всі данні від класу figure """
	def __init__(self, a, b):
		super(Square, self).__init__()
		self.a = a
		self.b = b

	def info_values_square(self):
		return f'{self.a}, {self.b}'

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