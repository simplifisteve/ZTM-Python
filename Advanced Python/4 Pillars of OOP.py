# # 4 Pillars of OOP

# # Encapsulation = package data and functions into attributes and methods (inside a class) to process data at scale
# # Abstraction = hiding away info and giving access to only what is necessary
# # Polymorphism = methods/functions/operators with the same name can be executed on many objects or classes

# class PlayerCharacter:
#     def __init__(self, name, age):
#         self._name = name  # underscore means private variable and should not be changed
#         self._age = age

#     def run(self):
#         print('run')

#     def speak(self):
#         print(f'My name is {self._name}, and I am {self._age} years young!')


# player1 = PlayerCharacter('Steve', 30)
# player1.speak()

# # Inheritance = let the instances use the attributes and methods of a class
# class User(object):
#     def __init__(self, email):
#         self.email = email

#     def sign_in(self):
#         print('logged in!')


# class Wizard(User):
#     def __init__(self, name, power, email):
#         super().__init__(email)  # "super" calls for the class a level above current class
#         self.name = name
#         self.power = power

#     def attack(self):
#         print(f'attacking with power of {self.power}')


# class Archer(User):
#     def __init__(self, name, num_arrows, email):
#         super().__init__(email)
#         self.name = name
#         self.num_arrows = num_arrows

#     def attack(self):
#         print(f'attacking with arrows: arrows left - {self.num_arrows}')


# wizard1 = Wizard('Merlin', 80, 'merlin@gmail.com')
# print(wizard1.attack())
# archer1 = Archer('Robin', 100, 'robin@gmail.com')
# print(archer1.attack())

# Introspection = determine the type of object at runtime & output list of access
# print(dir(wizard1))

# Dunder Methods = allow instances to interact with built-in functions and operators

# class Toy():
#     def __init__(self, color, age):
#         self.color = color
#         self.age = age
#         self.my_dict = {
#             'name': 'Yoyo',
#             'has_pets': False
#         }

#     def __str__(self):
#         return f'{self.color}'

#     def __len__(self):
#         return 5

#     def __call__(self):
#         return ('yesss??')

#     def __getitem__(self, i):
#         return self.my_dict[i]


# action_figure = Toy('red', 0)
# print(action_figure.__str__())
# print(str(action_figure))
# print(len(action_figure))
# print(action_figure())
# print(action_figure['name'])

# # Exercise: Extending List
# class SuperList(list):
#     def __len__(self):
#         return 1000


# super_list1 = SuperList()
# print(len(super_list1))
# super_list1.append(5)
# print(super_list1[0])
# print(issubclass(SuperList, list))

# # Multiple Inheritance = let an instance access methods/functions of the class and other instances
# class User(object):
#     def sign_in(self):
#         print('logged in!')


# class Wizard(User):
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power

#     def attack(self):
#         print(f'attacking with power of {self.power}')


# class Archer(User):
#     def __init__(self, name, arrows):
#         self.name = name
#         self.arrows = arrows

#     def check_arrows(self):
#         print(f'{self.arrows} remaining')

#     def run(self):
#         print('ran really fast')


# class HybridBorg(Wizard, Archer):
#     def __init__(self, name, power, arrows):
#         Archer.__init__(self, name, arrows)
#         Wizard.__init__(self, name, power)


# hb1 = HybridBorg('Wolfie', 50, 100)
# print(hb1.sign_in())
# print(hb1.power)
# print(hb1.arrows)

# MRO - Method Resolution Order = very complex and rarely used in good codes
# class A:
#     num = 10


# class B(A):
#     pass


# class C(A):
#     num = 1


# class D(B, C):
#     pass


# print(D.mro())
