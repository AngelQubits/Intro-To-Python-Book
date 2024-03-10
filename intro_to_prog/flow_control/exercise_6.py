def upcase(string):
	if len(string) >= 10:
		return string.upper()
	else:
		return string

print(upcase('hello world'))
print()
print(upcase('goodbye'))