# Error Handling
while True:
    try:
        age = int(input('What is your age? '))
        10/age
        # raise Exception('hey cut it out')  # very rarely used
    except ValueError:
        print('Please enter a number')
    except ZeroDivisionError:
        print('Please enter age higher than 0!')
    else:
        print('Thank you!')
        break
    # finally:
    #     print('Okay, I am finally done!')

# Handling multiple error types in one line
# def sum(num1, num2):
#     try:
#         return num1 + num2
#     except (TypeError, ZeroDivisionError) as err:
#         print(err)


# print(sum(1, '2'))
