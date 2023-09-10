# Generators = generate a sequence of values over time
# Iteration of values happens one by one, not taking up much memory
# Generators are super useful for large sets of data because of speed

# def generator_func(num):
#     for i in range(num):
#         yield i*2  # yield pauses func and comes back when "next" is called


# g = generator_func(100)
# next(g)  # "next" can be called until the range ran out
# next(g)
# next(g)
# print(next(g))

# for item in generator_func(1000):
#     print(item)


# def special_for(iterable):  # for loop - under the hood
#     iterator = iter(iterable)
#     while True:
#         try:
#             print(iterator)
#             print(next(iterator)**2)
#         except StopIteration:
#             break


# special_for([1, 2, 3])

# range function - under the hood
# class MyGen():
#     current = 0

#     def __init__(self, first, last):  # init - under the hood
#         self.first = first
#         self.last = last

#     def __iter__(self):
#         return self

#     def __next__(self):  # next - under the hood
#         if MyGen.current < self.last:
#             num = MyGen.current
#             MyGen.current += 1
#             return num
#         raise StopIteration


# gen = MyGen(0, 100)
# for i in gen:
#     print(i)

def fib(number):  # Generator - Fib Sequence = memory efficient
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a  # placeholder for "a"
        a = b  # move "a" up the sequence to continue function
        b = temp + b  # generates new "b"


for x in fib(100):
    print(x)

# def fib2(number): # LIST - Fib Sequence = very taxing on system
#     a = 0
#     b = 1
#     result = []
#     for i in range(number):
#         result.append(a)
#         temp = a
#         a = b
#         b = temp + b
#     return result


# print(fib2(100))
