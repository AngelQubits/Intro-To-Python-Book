from pprint import pprint
my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)

my_str = list(my_str)
final = list(zip(my_str, my_list, my_tuple, my_range))
pprint(final)

#solution:
# line 7, converting string into list to make it readalbe for zip
