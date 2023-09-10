# Functional Programming = separate data and functions, focus on simplicity & transparency
# Building programs by applying and composing only functions
# Uses expressions (evaluated to produce a value) instead of statements (to assign variables)
# Clear & understandable code, easy to extend, easy to maintain
# Memory efficient and DRY

# Pure Functions
# 1. Given the same input, functions should always return the same output
# 2. Functions should not produce any side effects, meaning they should not interact with anything external to the functions.
# Overall, pure functions = less bugs. But, it's impossible to have them everywhere.

# def multiply_by2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item*2)
#     return new_list


# print(multiply_by2([1, 2, 3]))

# Map, filter, zip, reduce
# from functools import reduce

# my_list = [1, 2, 3]
# your_list = [10, 20, 30]
# their_list = [5, 4, 3]


# def multiply_by2(item):  # Map function
#     return item*2


# def only_odd(item):  # Filter function
#     return item % 2 != 0


# def accumulator(acc, item):  # Reduce function
#     print(acc, item)
#     return acc + item


# print(reduce(accumulator, my_list, 8))
# print(list(zip(my_list, your_list, their_list)))
# print(list(map(lambda item: item*2, my_list)))
# print(my_list)
# print(list(filter(lambda item: item % 2 != 0, my_list)))
# print(my_list)

# # Square the list
# my_list = [5, 4, 3]
# print(list(map(lambda item: item**2, my_list)))

# # List Sorting
# a = [(0, 2), (4, 3), (9, 9), (10, -1)]
# a.sort(key=lambda x: x[1])
# print(a)

# Comprehensions: list & set
# my_list = [param for param in iterable if condition]

# my_list = {char for char in 'hello'}
# print(my_list)
# my_list2 = {num*2 for num in range(0, 100)}
# print(my_list2)
# my_list3 = [num**2 for num in range(0, 100) if num % 2 == 0]
# print(my_list3)

# Comprehensions: dictionary
# simple_dict = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
#     'd': 4
# }
# my_dict = {k: v**2 for k, v in simple_dict.items()
#            if v % 2 == 0}

# my_dict = {num: num*2 for num in [1, 2, 3]}

# print(my_dict)

# Comprehensions Exercise - Show Duplicates Values
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = list(
    set([value for value in some_list
         if some_list.count(value) > 1]))
print(duplicates)
