#11. Write a script to remove duplicates from Dictionary.

# My Answer:

s = {1: 10, 2: 20, 3: 30, 4: 10, 5: 60, 6: 60}

finaly_s = dict()

for i in s.items():
	key = i[0]
	value = i[1]
	if value not in finaly_s.values():
		finaly_s[key] = value
print(finaly_s)		
