# 5. Написати функцію < fibonacci >, яка приймає один аргумент і виводить всі числа Фібоначчі, що не перевищують його.

# Моя відповідь:

def fibonacci(n):
	s = list()
	a = b = 1
	
	if n > 0:
		s += [a, b]
	
	while True:
		a, b = b, a + b
		if b > n:
			break	
		s.append(b)	
	return s
	

print(fibonacci(25))