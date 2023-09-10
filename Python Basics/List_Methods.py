# Lists = mutable, items can be modified
# Ordered sequences of any data types
li = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c']
li3 = [1, 2, 'a', True]

# Data Structure
# A containerized way to store and use data with pros and cons

# List Slicing & Indexing
amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]

amazon_cart[0] = 'laptop'
# slicing does not include the ending index, this would return 0,1, and 2
new_cart = amazon_cart[0:3]
# new_cart = amazon_cart[:] <= This [:] syntax creates a new copy
new_cart[0] = 'gum'
print(new_cart)
print(new_cart.index('grapes'))
print(amazon_cart)

# Matrix = multi-dimensional, useful in data science, image processing, and complex calc
matrix = [
    [1, 5, 1],
    [0, 1, 0],
    [1, 0, 1]
]
print(matrix[0][1])

# List methods
# https://www.w3schools.com/python/python_ref_list.asp
# List Methods only modify the list in-place; will not output new copies
basket = [1, 2, 3, 4, 5]

# Adding
new_basket = basket.append(100)
new_basket = basket.insert(5, 888)
new_basket = basket.extend([222, 888])

# Removing
basket.pop(2)
basket.remove(5)
basket.clear()

# Indexing
basket = ['a', 'b', 'c', 'f', 'd', 'e', 'd']
print(basket.index('e', 0, 5))  # indexing does not include ending index
print('d' in basket)
print('s' in 'Steve Vong is awesome!')

# Count
print(basket.count('d'))

# Sorting & Reversing
basket.sort()
basket.reverse()
print(basket)

print(sorted(basket))  # sorted function outputs a new array/list

# Another way to write sorted()
new_basket = basket.copy()  # same as basket[:]
new_basket.sort()
print(basket)
print(new_basket)

# Common List Patterns
basket = ['a', 'b', 'c', 'f', 'd', 'e', 'd']
basket.sort()
basket.reverse()
print(basket[::-1])  # list slicing outputs a new copy of original list
print(basket)

print(list(range(1, 101)))  # quick way to create a list, useful for loops

new_sentence = ' '.join(['hi', 'Steve', 'is', 'super', 'awesome'])
print(new_sentence)

# List Unpacking
a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a)
print(b)
print(c)
print(other)
print(d)

# None = really nothing
weapons = None
print(weapons)
