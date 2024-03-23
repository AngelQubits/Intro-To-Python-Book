pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

# Part 1
print(pets['Dog'])

# Part 2
#pets['Lizard'] = 'None'
#print(pets["Lizard"])

# Part 3
#pets['Lizard'] = '<silence>'
#print(pets["Lizard"])

# Review the .get method

result = pets.get('Lizard')
print(result)

result = pets.get('Lizard', '<silence>')
print(result)