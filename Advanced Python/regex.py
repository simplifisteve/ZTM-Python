import re

# "r" means raw string, interpreter will ignore everything else
# pattern = re.compile(r"([a-zA-Z]).([a])")
# string = "Hello world. How are you doing?"

# a = pattern.search(string)
# b = pattern.findall(string)
# c = pattern.fullmatch(string)
# d = pattern.match(string)
# print(a.span())  # index of where the string occurs
# print(b)  # find all instances of the pattern
# print(c)  # matches the entire string
# print(d)  # checks for a match, but not an exact full match
# print(a.group())

# # Advanced Patterns
# # https://www.w3schools.com/python/python_regex.asp
# # https://regex101.com/ # Regex generator and useful explanation
# # https://regexone.com/ # Interactive tutorials

# # Email Checker
pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = "qoobee@gmail.com"

a = pattern.search(string)
print(a)

# # Password Checker
pattern = pattern = re.compile(
    r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[$%#@])[A-Za-z\d$%#@]{8,}$")
password = "aBc123$%@"

if pattern.match(password):
    print("Password is valid")
else:
    print("Invalid password")
