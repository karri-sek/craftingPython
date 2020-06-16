x = { 'a': 4, 'b': 5, 'c': 7}
y = {'a': 5, 'b': 6, 'd': 8}

z = dict(x, **y)
print("z > ",z)

z = { **x , **y}

print (" z in new ", z)