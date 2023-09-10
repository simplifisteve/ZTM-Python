# Conditional Logic
age = 30
license = 'Indiana'

if age and license:
    print("You are old enough to drive, and you have a license!")
# elif condition:
# elif condition:
# as many elif as needed
else:
    print("You are not of age!")

# Truthy vs Falsy
# We use "truthy" and "falsy" to differentiate from the bool values True and False.
# A "truthy" value will satisfy the check performed by if or while statements.
# As explained in the documentation, all values are considered "truthy" except for the following, which are "falsy":

# None
# False
# Numbers that are numerically equal to zero, including:
# 0
# 0.0
# 0j
# decimal.Decimal(0)
# fraction.Fraction(0, 1)
# Empty sequences and collections, including:
# [] - an empty list
# {} - an empty dict
# () - an empty tuple
# set() - an empty set
# '' - an empty str
# b'' - an empty bytes
# bytearray(b'') - an empty bytearray
# memoryview(b'') - an empty memoryview
# an empty range, like range(0)
# objects for which
# obj.__bool__() returns False
# obj.__len__() returns 0, given that obj.__bool__ is undefined

# Ternary Operator = Conditional Expression
# Shortcut on certain conditional logic
# output_if_true if condition else output_if_else
is_friend = False
can_message = "messages allowed" if is_friend else "not allowed to message"
print(can_message)

# Short Circuiting
# Evaluate as many conditions as needed, if true, then ignore the rest to return an output
is_friend = False
is_user = True

if is_friend and is_user:
    print('Best friends forever!')

if is_friend or is_user:
    print('Best friends forever!')

# Logical Operators
# and, or, not, >, <, >=, <=, ==,!=

is_magician = True
is_expert = True

# check if magician AND expert
if is_magician and is_expert:
    print("You are a master magician!")
# check if magician but not an expert
elif is_magician and not is_expert:
    print("At least you're getting there ...")
# check if not a magician
elif not is_magician:
    print("You need magic powers!")

# == operator checks for equality of value
print(True == 1)
print('1' == 1)
print(10 == 10.0)
print([] == [])
print([1, 2, 3] == [1, 2, 3])

# is keyword checks for location in memory
print(True is 1)
print('1' is 1)
print(10 is 10.0)
print([] is [])
print([1, 2, 3] is [1, 2, 3])
