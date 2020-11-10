#4. Write a script to concatenate N strings.

# My Answer:

N = int(input("Введіть кількість строк "))

P = str()
for _ in range(N):
	P += str(input())
print(P)
