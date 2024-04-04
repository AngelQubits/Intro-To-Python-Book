from pprint import pprint
my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

# using for loop iterate through my_list
# check if element is odd or even
# if odd append string 'odd' to list called new_list
# print new_list

new_list = []

for x in my_list:
	if x % 2 == 0:
		new_list.append('even')
	else:
		new_list.append('odd')
pprint(new_list)