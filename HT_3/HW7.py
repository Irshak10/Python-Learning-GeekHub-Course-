# 7. Написати функцію, яка приймає на вхід список і підраховує кількість однакових елементів у ньому.

# Моя відповідь:

from collections import Counter


def same_elements(n):
	return Counter(n)


print(same_elements([1, 2, 1, 2, 2, 2, 3, 4, 5]))