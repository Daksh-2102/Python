#Itertools :- product, permutations, combination, accumulate, groupby, and infinite iterators.

from itertools import product

a = [1,2]
b = [3,4]

pro = product(a,b)

print(list(pro))  