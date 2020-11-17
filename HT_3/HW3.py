#3.Написати функцию < is_prime >, яка прийматиме 1 аргумент - число від 0 до 1000, и яка вертатиме True, якщо це число просте, и False - якщо ні.

#Моя відповідь:


def is_prime(n):
	
	if n == 2:
		return True
	elif n < 2:
		return False

	for i in range(2, n):
		if n % i == 0:
			return False
				
	return True
			
		
print(is_prime(4))