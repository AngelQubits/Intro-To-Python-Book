# Use slicing to write Python code to print a 6-character substring of 
#'Launch School' that begins with the first c.

ls = 'Launch School'
print(ls[4:10])

# Find index programatically
ls1 = ls.find('c')
print(ls[ls1:ls1 + 6])
