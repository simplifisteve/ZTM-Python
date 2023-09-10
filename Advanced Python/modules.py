from collections import Counter, defaultdict, OrderedDict
import datetime
import array
import pdb

print(datetime.datetime.now())

# li = [1, 2, 3, 2, 1, 4, 5, 2, 1]
# sentence = "Qoobee is super cute"
# print(Counter(li))
# print(Counter(sentence))

# dictionary = defaultdict(lambda: 'does not exist', {'a': 1, 'b': 2, 'c': 3})
# print(dictionary['e'])

# d = OrderedDict()
# d['a'] = 1
# d['b'] = 2

# d2 = OrderedDict()
# d2['a'] = 1
# d2['b'] = 2

# print(d2 == d)

# Dictionaries are now ordered by default in Python 3.7+

# Array of integers
numbers = array.array('i', [1, 2, 3])
print(numbers[1])

# pdb is really to debug code, set breakpoints and step through code
# pdb.set_trace()
