my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

for x in my_list:
	for y in x:
		if y % 2 == 0:
			print(y)