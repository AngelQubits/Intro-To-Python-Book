# will print out 'Holy Grail'
# since dict2 is a shallow copy of dict1, any changes on dict2
# will be reflectedon dict1

# I failed to understand the difference between two variables referencing
# eachother as in the previous example, and shallow copies being two separate
# objects where changes to one do not affect the other.
# in this case dict1 == dict2 is False, because dict1 is dict2 is also false.
import copy

a=[1, 2]
b = a
c = copy.copy(a)

print(b is a)
print(b == a)
# should both be true

print(c is a)
print(c == a)

# False
# True