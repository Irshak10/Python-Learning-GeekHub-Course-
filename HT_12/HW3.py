# -*- coding: utf-8 -*-

# 3. Створіть за допомогою класів та продемонструйте свою реалізацію шкільної бібліотеки(включіть фантазію).

# Моя відповідь: 


class Library(object):
	"""Батьківський клас"""
	def __init__(self, name, pages, status):
		self.name = name
		self.pages = pages
		self.status = status
		
	def info(self):
		return f'Назва: {self.name}, і містить {self.pages} сторінок. Статус: {self.status}'

	def rent(self):
		self.status = 'rented'
		return f'Майно бібліотеки взято в аренду, тому його статус змінився на: {self.status}'

	def turn_back(self):
		self.status = 'free'
		return f'Майно бібліотеки повернено з аренди, тому його статус змінився на: {self.status}'

class Book(Library):
	"""Дочірній клас Book, який унаслідував всі данні від класу Library, з додатковим атребутом"""
	def __init__(self, name, pages, status, lesson):
		super(Book, self).__init__(name, pages, status)
		self.lesson = lesson

	def type_of_item(self):
		return (f'Це книга, з предмету: {self.lesson}')

class Magazine(Library):
	"""Дочірній клас Magazine, який унаслідував всі данні від класу Library"""
	def type_of_item(self):
		return ('Це журнал')


a = Library('Test', 165, 'free')
print(a.info())
print()

b = Book('The mountains', 120, 'free', 'Geography')
print(b.info())
print(b.type_of_item())
print(b.rent())
print(b.info())
print(b.turn_back())
print(b.info())
print()

d = Book('The Python', 150, 'free', 'Computer Science Lesson')
print(d.info())
print(d.type_of_item())
print(d.rent())
print(d.info())
print(d.turn_back())
print(d.info())
print()

c = Magazine('Marvel', 50, 'free')
print(c.info())
print(c.type_of_item())
print(c.rent())
print(c.info())
print(c.turn_back())
print(c.info())