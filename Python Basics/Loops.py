# Loops
# Run lines of codes over and over really fast
# Iterable = collection of items that can be processed over and over
# Iterated = one by one check each item in the collection

# # For Loop
# for item in {1, 2, 3, 4, 5}:
#     for x in ['a', 'b', 'c']:
#         print(item, x)

# user = {
#     'name': 'Goma',
#     'age': 9177,
#     'can_swim': True
# }

# for key, value in user.items():
#     print(key, value)

# for item in user.values():
#     print(item)

# for item in user.keys():
#     print(item)

# # Counter Exercise
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# counter = 0

# for item in my_list:
#     counter = counter + item
# print(counter)

# range()
# for number in range(0, 100, 2):
#     print(number)

# for _ in range(10, 0, -2):
#     print(_)

# for _ in range(2):
#     print(list(range(10)))

# enumerate()
# for i, char in enumerate(list(range(100))):
#     if char == 50:
#         print(f'index of 50 is: {i}')

# # While Loops = useful for very long looping
# i = 0
# while i < 50:
#     print(i)
#     # break
#     i += 1
# else:
#     print('Done with all the work!')

# # While Loop vs For Loop
# my_list = [1, 2, 3]
# for item in my_list:
#     print(item)

# i = 0
# while i < len(my_list):
#     print(my_list[i])
#     i += 1

# while True:
#     response = input('say something: ')
#     if (response == 'bye'):
#         break

# # break, continue, pass
# # break = break completely out of a loop
# # continue = continue to go back to the loop
# # pass = very rarely used, can be a useful placeholder for "thinking about it"

# # First GUI Practice
# picture = [
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 1, 1, 1, 0, 0],
#     [0, 1, 1, 1, 1, 1, 0],
#     [1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0]
# ]


# fill = '*'
# empty = ' '

# for row in picture:
#     for pixel in row:
#         if pixel:
#             print(fill, end=' ')
#         else:
#             print(empty, end=' ')
#     print(empty)  # to start a new line after each row

# # To create a heart
# love = 'PhuLovesNhi'
# print('\n'.join([''.join([(love[(x-y) % len(love)]
#                            if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ')
#                           for x in range(-30, 30)])
#                  for y in range(15, -15, -1)]))

# # Exercise - Find Duplicates
# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# unique = []
# duplicates = []

# for i in some_list:
#     if i not in unique:
#         unique.append(i)
#     else:
#         duplicates.append(i)
# print("Unique Item List", unique)
# print("List of duplicates", duplicates)

# duplicates = []

# for value in some_list:
#     if some_list.count(value) > 1:
#         if value not in duplicates:
#             duplicates.append(value)
# print(duplicates)
