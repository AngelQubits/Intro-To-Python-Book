ans1 = input("Enter the first number: ")
ans2 = input("Enter the second number: ")

def multiply(first, second):
    first = float(first)
    second = float(second)
    print(first, '*', second, "=", first * second)
    return first * second
    
multiply (ans1, ans2)