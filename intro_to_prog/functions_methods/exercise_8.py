print("this piece of code will cause an error due to, too many arguments")

def foo(bar, qux):
    print(bar)
    print(qux)

foo(42, 3.141592, 2.718)