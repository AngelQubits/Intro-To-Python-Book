# Updated age.py
#pseudocode:
#for x in range(10, 50, 10):
#take input in age variable
#print out string you are age years old.
#you will then loop throug range 10 thru 40
#print out in x you will be age + x statement.

age = input("How old are you? ")
print(f"You are {age} years old. \n")
for x in range(10, 50, 10):
	print(f"In {x} years, you will be", (x + int(age)), "years old. ")
	
	