foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)

print("this code prints 'bar', because it is defined in outerscope"
      " the inner scope variable is not doing anything."
)