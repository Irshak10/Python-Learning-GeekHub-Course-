#8. Write a script to replace last value of tuples in a list.
#		Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
#		Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

# My Answer:

a = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
b = list()

for i in a:
	k = list(i)
	k[-1] = 100
	m = tuple(k)
	b.append(m)
print(b)
