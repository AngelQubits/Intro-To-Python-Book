# will print out [1, 42,3]

# reason is because dict2 is a shallow copy, and as a result
# complex objects within dict1 and dict2 are referencing the same object 
# on heap.