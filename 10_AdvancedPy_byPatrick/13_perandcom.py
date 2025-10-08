#Permutation and combinations using itertools

from itertools import permutations

a = (1,2,3)
per = permutations(a,2) # 2--> SET OF 2

print(list(per))


#Combinations

from itertools import combinations

b = (4,5,6)

comb = combinations(b,2)

print(list(comb))