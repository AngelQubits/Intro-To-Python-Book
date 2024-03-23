from pprint import pprint
# print activities cocoa enjoys

cats = {
    'Pete': {
        'Cheddar': {
            'color': 'orange',
            'enjoys': {
                'sleeping',
                'snuggling',
                'meowing',
                'eating',
                'birdwatching',
            },
        },
        'Cocoa': {
            'color': 'black',
            'enjoys': {
                'eating',
                'sleeping',
                'playing',
                'chewing',
            },
        },
    },
}
#pprint(cats.keys())
#print()
#pprint(cats.values())
#print()
#pprint(cats.items())
#print()

#result = cats['Pete']['Cocoa']['enjoys']
print(cats['Pete']['Cocoa']['enjoys'])