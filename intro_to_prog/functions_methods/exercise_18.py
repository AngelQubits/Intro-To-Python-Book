def remainders_3(numbers):
    return [number % 3 for number in numbers]
    
numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []

ans1 = print(any(remainders_3(numbers_1)))
ans2 = print(any(remainders_3(numbers_2)))
ans3 = print(any(remainders_3(numbers_3)))
ans4 = print(any(remainders_3(numbers_4)))