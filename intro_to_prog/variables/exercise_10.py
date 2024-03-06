print("reassign - strings not mutable")
print("reassign - strings not mutable")
print("reassign - strings not mutable")
print("neither")
print("mutable - object is now a list")
print("mutable - object now empty list due to .pop")
print("neither - index error")
print("neither - nothing to sort")
print("mutable - object now a set")
print("mutable - object now a tuple")

print("Solution: ")

#obj = 'ABcd'      $ Reassignment
#obj.upper()       $ Neither - calling method on string does nothing
#obj = obj.lower() $ Reassignment - the equal sign assigns, hence, reassigns.
#print(len(obj))   $ Neither
#obj = list(obj)   $ Reassignment - note equal sign reassigns in this case.
#obj.pop()         $ Mutation
#obj[2] = 'X'      $ Mutation
#obj.sort()        $ Mutation
#set(obj)          $ Neither
#obj = tuple(obj)  $ Reassignment