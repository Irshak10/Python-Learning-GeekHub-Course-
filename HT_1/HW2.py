# 2. Write a script to print out a set containing all the colours from color_list_1 which are not present in color_list_2.

#		Expected Output :
#		{'Black', 'White'}

# My Answer:

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

a = (color_list_1 - color_list_2)
print(a)
