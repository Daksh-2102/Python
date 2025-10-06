# collections : Counter , namedtuple , OrderedDict , defaultdict , deque

# 1 counter : is a in-bulit fnx that returns the no. of occurences in that str of each char as dict values

from collections import Counter

str = "aaaaabbbbccc"
count = Counter(str)

print(count)