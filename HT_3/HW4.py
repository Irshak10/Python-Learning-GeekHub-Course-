#4. Написати функцію < prime_list >, яка прийматиме 2 аргументи - початок і кінець діапазона, і вертатиме список простих чисел всередині цього діапазона.

# Моя відповідь:


def prime_list(start, finish):
	s = list()
	for i in range(start, finish + 1):
		
		if i == 2:
			s.append(i)
		elif i < 2:
			continue
		else:
			r_num = True
			for n in range(2, i):
				if i % n == 0:
					r_num = False
					break
		
			if r_num:
				s.append(i)
	
	return s


print(prime_list(0,100))