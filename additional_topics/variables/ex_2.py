# set2 is pointing to set1, as a result changes taking place to set1
# will be reflected on set2

list1 = ['a', 'b', 1]
list2 = list1
print(list2)

list2.append('x')
print(list2)
print(list1)

# Insight:  changes to list2 will also be reflected on list1 both are pointing
# to same address in memory.