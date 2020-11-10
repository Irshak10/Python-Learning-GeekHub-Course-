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
