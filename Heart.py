love = 'NhiLovesPhu'
print('\n'.join([''.join([(love[(x-y) % len(love)]
                           if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ')
                          for x in range(-30, 30)])
                 for y in range(15, -15, -1)]))


# def highest_even(li):
#     # even = [x for x in li if x % 2 == 0]
#     # print("Highest even number is ", max(even))
#     # print("Highest even number is: ",
#     #       max(filter(lambda x: x % 2 == 0,li)))
#     evens = []
#     for item in li:
#         if item % 2 == 0:
#             evens.append(item)
#     return max(evens)


# print(highest_even([10, 2, 3, 4, 8, 11, 128, 222, 917]))
