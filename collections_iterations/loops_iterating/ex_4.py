# adjust while loop to select even numbers

my_list = [6, 3, 0, 11, 20, 4, 17]
start = 0

print('While Even Loop Example: ')
while start < len(my_list):
	if my_list[start] % 2 == 0:
		print(my_list[start])
	start += 1

#adjust for loop to select odd numbers
print()
print('For Odd Loop Example: ')

for x in my_list:
	if x % 2 != 0:
		print(x)
		
