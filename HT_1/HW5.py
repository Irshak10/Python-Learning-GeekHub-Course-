#5. Write a script to convert decimal to hexadecimal

# My Answer:

a = int(input())
b = hex(a)

if 0<=a<=9:
	print("0" + b[2:])
else:
	print(b[2:])
