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