love = 'NhiLovesPhu'

for y in range(15, -15, -1):
    line = ''
    for x in range(-30, 30):
        index = (x-y) % len(love)
        char = love[index] if ((x*0.05)**2+(y*0.1)**2-1)**3 - \
            (x*0.05)**2*(y*0.1)**3 <= 0 else ' '
        line += char
    print(line)


# def highest_even(li):
#     evens = [x for x in li if x % 2 == 0]
#     return max(evens)


# print(highest_even([10, 2, 3, 4, 8, 11, 128, 222, 917]))
