# EXERCISES
# 1 Capitalize all of the pet names and print the list
from functools import reduce
my_pets = ['sisi', 'bibi', 'titi', 'carla']
capitalized = []
for item in my_pets:
    capitalized.append(item.capitalize())
print(capitalized)

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]
sorted_numbers = my_numbers.sort()
print(tuple(zip(my_strings, my_numbers)))

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def passing_scores(item):
    return item > 50


print(list(filter(passing_scores, scores)))
# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores).
# What is the total?


def accumulator(my_numbers, item):
    print(my_numbers, item)
    return my_numbers + item


print(reduce(accumulator, scores + my_numbers, 0))
