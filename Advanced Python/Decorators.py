# Decorators = wrap another function in order to extend the behavior of wrapped function, without permanently modifying it
# Functions = first class objects = can be used or passed as arguments
# Higher Order Function = accepts or returns another function

# def my_decorator(func):
#     def wrap_func(*args, **kwargs):
#         print('********')
#         func(*args, **kwargs)
#         print('********')
#     return wrap_func


# @my_decorator
# def hello(greeting, emoji=':)'):
#     print(greeting, emoji)


# hello('hiii')

# from time import time


# def performance(fn):
#     def wrapper(*args, **kwargs):
#         t1 = time()
#         result = fn(*args, **kwargs)
#         t2 = time()
#         print(f'Function took {t2-t1} s')
#         return result
#     return wrapper


# @performance
# def long_time():
#     for i in range(1000000):
#         i * 5


# long_time()

# Authenticator Exercise
user1 = {
    'name': 'Sorna',
    'valid': True  # changing this will either run or stop the function
}

user2 = {
    'name': 'Goma',
    'valid': False
}

user3 = {
    'name': 'Peach',
    'valid': True
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid']:  # dependent on user1
            return fn(*args, **kwargs)
        else:
            print('You are not allowed to send messages!')
    return wrapper


@authenticated
def message_friends(user):
    print(f'Message has been sent, {user["name"]}!')


message_friends(user1)
message_friends(user2)
message_friends(user3)
