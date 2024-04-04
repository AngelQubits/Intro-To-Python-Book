# write function
# returns factorial of number using for loop
# argument always integer

# def function that takes n as argument
# define the iterable range starting at 1 : n+1
# result as multiplying variable times new x

def factorial(n):
	result = 1
	for x in range(1, (n + 1)):
		result *= x
	print(result)

factorial(8)