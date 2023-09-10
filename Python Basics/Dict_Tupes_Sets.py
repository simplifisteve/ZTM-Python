# {key:value} = dictionaries
# {} = sets = unordered collection of unique items
# [] = lists
# () = tuples = immutable lists but faster than lists

# Dictionaries = unordered containers of key:value pairs
dictionary = {
    'a': [1, 2, 3],
    'b': "Hello World!",
    'x': True
}

my_list = [
    {
        'a': [1, 2, 3],
        'b': "Hello World!",
        'x': True
    },
    {
        'a': [7, 8, 9],
        'b': "Steve is super awesome!",
        'x': True
    }
]

print(my_list[1]['b'])
print(dictionary['a'][1])

# Dictionary Keys
# Must be immutable, meaning keys cannot be changed
# Keys must also be unique, otherwise, values will be overwritten
# Data types for keys can be str, int, etc but not lists
# BUT, 99% of time a key is something descriptive, like 'Goma'

# Dictionary Methods
user = {
    'keys': [1, 2, 3],
    'greet': 'hello',
    'age': 20
}

user2 = dict(name="Steve Vong")  # uncommon way to create a dictionary

print(user.get('age', 30))
print(user2)

print('hello' in user.values())
print('age' in user.keys())

print(user.items())
print(user.clear())

print(user.pop('age'))
print(user)

# Removes the last item in the dictionary, updated since Python 3.7
print(user.popitem())
print(user)

print(user.update({'age': 30, 'Country': "Vietnam"}))
print(user)

# Tuples
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple.count(5))
print(my_tuple.index(3))
print(len(my_tuple))

x, y, z, *other = (1, 2, 3, 4, 5)
print(other)

# Sets
my_set = {1, 2, 3, 3, 4, 5, 5, 6, 7, 8, 8}
print(my_set)  # only unique items will be returned

my_list = [1, 2, 3, 4, 5, 5]
print(set(my_list))  # removes duplicates from a list

my_set = {1, 2, 3, 4, 5, 5}
new_set = my_set.copy()
my_set.clear()
print(new_set)
print(my_set)

# Set Methods = Venn Diagramming, similar to SQL
my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

print(my_set.difference(your_set))  # shows the difference between 2 sets

your_set.discard(8)
print(your_set)

my_set.difference_update(your_set)  # removes the differences
print(my_set)

print(my_set.intersection(your_set))  # shows the values existing in both sets
print(my_set & your_set)  # shorthand way to write intersection()

print(my_set.isdisjoint(your_set))  # are the sets NOT overlapping?

print(my_set.union(your_set))
print(my_set | your_set)  # shorthand way to write union()

print(my_set.issubset(your_set))
print(your_set.issuperset(my_set))
