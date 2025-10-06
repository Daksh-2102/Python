# collections : Counter , namedtuple , OrderedDict , defaultdict , deque

# 1 counter : is a in-bulit fnx that returns the no. of occurences in that str of each char as dict values

from collections import Counter

str = "aaaaabbbbccc"
count = Counter(str) 

print(count)   #Counter({'a': 5, 'b': 4, 'c': 3})

print(count.keys()) #dict_keys(['a', 'b', 'c'])

print(count.items()) #dict_items([('a', 5), ('b', 4), ('c', 3)])

print(count.values()) #dict_values([5, 4, 3])

#to check the most common elements
print(count.most_common(1)) # 1 -> THE most common one element
