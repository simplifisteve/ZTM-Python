# Integer and float
import datetime
print(type(2 + 4))
print(type(2 - 4))
print(type(2 * 4))
print(type(2 / 4))

# Exponential
print(2 ** 2)
# Floor division
print(5 // 4)
# Remainder of or Modulus
print(6 % 4)

# Math Operations
print(round(3.1))
print(abs(-9.99))

# Order of Operations
# PEMDAS: (), **, * or /, + or -

# To get the binary representation
print(bin(5))
# To return the integer from binary
print(int('0b101', 2))

# Variables
# snake_case
# Start with underscore or lowercase
# Letters, numbers, underscores
# Case sensitive
# Don't overwrite Python keywords
IQ = 190
print(IQ)

# Constants = never change once assigned
# Ex: PI = 3.14

# Dunders = double underscored variables
# Don't overwrite [dunders](https://mathspp.com/blog/pydonts/dunder-methods)

# Expression = the part of the statement that produces a value
# Statement = an entire line of code

# Augmented Assignment Operator
some_value = 8
some_value += 2
some_value -= 2

# Type Conversion
print(type(int(str(100))))

# Formatted Strings
name = "Steve"
age = 30
print(
    f'Hello {name} you are {age} years young! Get to work. Build your wealth!!!')

# String Indexes and Slicing
# [start:stop:stepover]
awesome = '0123456'
print(awesome[0:7:2])  # start at 0, go to 7, stepover by 2
print(awesome[1:])  # start at 1, go all the way to the end
print(awesome[:5])  # go all the way to 5
print(awesome[::1])  # start:stop, stepover by 1
print(awesome[-1])  # negative index = start in reverse
print(awesome[::-1])  # start:stop, go in reverse

# Immutability
# Str in Python cannot be changed, meaning ...
awesome = '0123456'  # cannot be partially changed, only completely re-assigned

# Built-in Functions
greet = 'helloooo'
print(greet[0:len(greet)])  # length of 9

# String Methods
# Automatic tools to use on str
# For example, .format()
quote = 'to be or not to be'
print(quote.upper())
print(quote.replace('be', 'drive'))

# Booleans True/False
# bool(1) = True
# bool(0) = False

# Type Conversion Exercise
today = datetime.date.today()
year = today.year
name = input('What is your first name? ')
birth_year = input('What year were you born in? ')
age = year - int(birth_year)
print(f'Hello {name}! You are now {age} years young!!')

# Password Checker Exercise
username = input('What is your username? ')
password = input('Paste in your password here: ')
length = len(password)
password_hidden = '*' * len(password)
print(
    f'Hello {username}! Your password {password_hidden} is {length} characters long.')
