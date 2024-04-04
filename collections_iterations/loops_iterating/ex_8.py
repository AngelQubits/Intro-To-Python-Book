# write a dict compreneshion x = {str : len(k) for x in set}
# select for only keys with % 2 not 0

my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

odd_keys = {x : len(x)
            for x in my_set
            if len(x) % 2 != 0}
print(odd_keys)