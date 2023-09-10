# # Functions = modify or return something

# picture = [
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 1, 1, 1, 0, 0],
#     [0, 1, 1, 1, 1, 1, 0],
#     [1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0]
# ]


# def show_tree():
#     fill = '*'
#     empty = ' '

#     for row in picture:
#         for pixel in row:
#             if pixel:
#                 print(fill, end=' ')
#             else:
#                 print(empty, end=' ')
#         print(empty)


# show_tree()

# # Parameters = used to define a function
# def say_hello(name='Panda', emoji='🐻‍❄️'):
#     print(f'Hello {name} {emoji}')


# say_hello()


# def say_hello(name, emoji):
#     print(f'Hello {name} {emoji}')


# # Arguments = actual values to call a function
# # Positional arguments = need to be in proper places
# say_hello('Be Phu', '🥰❤️')
# # Keyword arguments
# say_hello(name='Steve', emoji='😋')

# # return function
# def sum(num1, num2):
#     return num1 + num2


# print(sum(8, 10))

# # Single-responsibility principle
# # A function should do one thing really well
# # A function should also return something

# def sum(num1, num2):
#     def another_func(n1, n2):
#         return n1 + n2
#     return another_func(num1, num2)


# # # return function will automatically exit a function
# total = sum(10, 20)
# print(total)

# Exercise - checkDriverAge
# def checkDriverAge(age=0):
#     if int(age) < 18:
#         print("Sorry, you are too young to drive this car. Powering off!")
#     elif int(age) > 18:
#         print("Powering On. Enjoy the ride!")
#     elif int(age) == 18:
#         print("Congrats on your first year of driving. Enjoy the ride!")


# checkDriverAge(16)

# # Methods vs Functions
# # Methods have to be owned by something (objects, data types, etc.)
# # Functions modify or return something

# # Doc-strings = add comments and definitions to user-defined functions
# def test(a):
#     '''
#     Info: this function tests and prints param a
#     '''
#     print(a)

# help(test)
# print(test.__doc__)

# # CLEAN code
# def is_even(num):
#     return num % 2 == 0  # returns True or False by default


# print(is_even(30))

# # Unnecessary code => not utilizing default features
# def is_even(num):
#   if num % 2 == 0:
#     return True
#   else:
#     return False
# print(is_even(30))

# # *args and **kwargs
# # *args = as many arguments as desired
# # **kwargs = as many keyword arguments as desired

# def super_func(*args, **kwargs):
#     total = 0
#     for items in kwargs.values():
#         total += items
#     return sum(args) + total


# print(super_func(2, 4, 6, 8, 10, num1=5, num2=10))

# # Rule: params, *args, default parameters, **kwargs

def highest_even(li):
    # even = [x for x in li if x % 2 == 0]
    # print("Highest even number is: ", max(even))
    print("Highest even number is: ",
          max(filter(lambda x: x % 2 == 0, li)))
    # evens = []
    # for item in li:
    #     if item % 2 == 0:
    #         evens.append(item)
    # return max(evens)


print(highest_even([10, 2, 3, 4, 8, 11]))
