def number_range(x):
	if (x >= 0) and (x <= 50):
		print(f'{x} is between 0 and 50 \n')
	elif (x >= 51) and (x <= 100):
		print(f'{x} is between 51 and 100 \n')
	elif (x >= 100):
		print(f'{x} is greater than 100 \n')
	else:
		print(f'{x} is less than 0 \n')

number_range(0)
number_range(25)
number_range(50)
number_range(75)
number_range(100)
number_range(101)
number_range(-1)