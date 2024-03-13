print("Not directly. Tuples are immutable \n")

stuff = ('hello', 'world', 'bye', 'now')
print(stuff)
stuff = list(stuff)
stuff[2] = 'goodbye'
stuff = tuple(stuff)
print()
print(stuff)