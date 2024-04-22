def sum_of_squares(num1, num2):
	    def square(x):
		    result = x ** 2
		    return result
	    return square(num1) + square(num2)
	

print(sum_of_squares(3, 4))   # 25 (3 * 3 + 4 * 4)
print(sum_of_squares(5, 12))  # 169 (5 * 5 + 12 * 12)