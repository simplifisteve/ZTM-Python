# OOP, attributes, and methods
# Everything in Python comes from the base "object"

class PlayerCharacter:
    # Class Object Attribute (static)
    membership = True  # applies to all instances
    # age = 18

    def __init__(self, name='anonymous', age=0):  # constructor function
        if (age > 18):
            self.name = name  # self refers to the instance
            self.age = age  # attributes are dynamic & specific to each object

    def shout(self):
        print(f'My name is {self.name}')
        return 'continue'

    @classmethod  # global, can be applied to Class without instantiating
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2

# player1 = PlayerCharacter('Phu', 30)
# player2 = PlayerCharacter('Nhi', 32)


# print(PlayerCharacter.adding_things(3, 5))
print(PlayerCharacter.age)
