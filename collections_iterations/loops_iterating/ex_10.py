# simplify this code so you don't use randrange twice
# simplify by looping it for a known amount range (1, 3)

import random

highest = 10

while True: 
	number = random.randrange(highest + 1)
	print(number)
	
	if number == highest: 
	    break

	