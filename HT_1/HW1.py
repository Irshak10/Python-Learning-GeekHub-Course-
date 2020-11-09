#-----------------------------------------------------------------------------------------------------------------------------
# 1 .Write a script which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

# My Answer:

a = input().split(',')
print(a)
print(tuple(a))

#-----------------------------------------------------------------------------------------------------------------------------
# 2. Write a script to print out a set containing all the colours from color_list_1 which are not present in color_list_2.

#		Expected Output :
#		{'Black', 'White'}

# My Answer:

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

a = (color_list_1 - color_list_2)
print(a)

#-----------------------------------------------------------------------------------------------------------------------------
# 3. Write a script to sum of the first n positive integers.

# My Answer:

n = int(input())
sum_positive = (n * (n + 1)) / 2
print(sum_positive)

#-----------------------------------------------------------------------------------------------------------------------------
#4. Write a script to concatenate N strings.

# My Answer:

N = int(input("Введіть кількість строк "))

P = str()
for _ in range(N):
	P += str(input())
print(P)

#-----------------------------------------------------------------------------------------------------------------------------
#5. Write a script to convert decimal to hexadecimal

# My Answer:

a = int(input())
b = hex(a)

if 0<=a<=9:
	print("0" + b[2:])
else:
	print(b[2:])

#-----------------------------------------------------------------------------------------------------------------------------
#6. Write a script to check whether a specified value is contained in a group of values.
#		Test Data :
#		3 -> [1, 5, 8, 3] : True
#		-1 -> (1, 5, 8, 3) : False

# My Answer:

a = [1, 5, 8 ,3]
n = int(input())

if n in a:
	print(True)
else:
	print(False)

#-----------------------------------------------------------------------------------------------------------------------------
#7. Write a script to concatenate all elements in a list into a string and print it.

# My Answer:

a = ['Test','Double Test','Triple Test']
print(' '.join(a))

#-----------------------------------------------------------------------------------------------------------------------------
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

#-----------------------------------------------------------------------------------------------------------------------------
#9. Write a script to remove an empty tuple(s) from a list of tuples.
#		Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
#		Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']

# My Answer:

a = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]

b = []
for i in a:
	if i:
		b.append(i)
print(b)

#-----------------------------------------------------------------------------------------------------------------------------
#10. Write a script to concatenate following dictionaries to create a new one.
#		Sample Dictionary :
#		dic1={1:10, 2:20}
#		dic2={3:30, 4:40}
#		dic3={5:50,6:60}
#		Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# My Answer:

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50,6:60}

new_dic = dict()
for i in [dic1,dic2,dic3]:
	new_dic.update(i)
print(new_dic)

#-----------------------------------------------------------------------------------------------------------------------------
#11. Write a script to remove duplicates from Dictionary.

# My Answer:

dic = {1: 10, 2: 20, 3: 30, 4: 10, 5: 60, 6: 60}
a = dic.values()
b = set(a)

print(b)

#-----------------------------------------------------------------------------------------------------------------------------
#12. Write a script to concatenate following dictionaries to create a new one.
#		Sample Dictionary :
#		dic1={1:10, 2:20}
#		dic2={3:30, 4:40}
#		dic3={5:50,6:60}
#		Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# My Answer (dublicate tack #10):

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50,6:60}

new_dic = dict()
for i in [dic1,dic2,dic3]:
	new_dic.update(i)
print(new_dic)

#-----------------------------------------------------------------------------------------------------------------------------
#13. Write a script to get the maximum and minimum value in a dictionary.

# My Answer:

a = {1: 500, 2: 20, 3: 355, 4: 299, 5: 500, 6: 6000}
value_min = min(a.values())
value_max = max(a.values())

print('Мінімальні значення', value_min)
print('Максимальні значення', value_max)

#-----------------------------------------------------------------------------------------------------------------------------
#14. Write a script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
#		Sample Dictionary ( n = 5) :
#		Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# My Answer:

n = int(input())
a = dict()

for x in range(1,n+1):
	a[x]=x*x
print(a)