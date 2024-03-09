print("This piece of code generates an error due to lack of 3rd argument")

def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)