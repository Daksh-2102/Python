#Sets are collection of data types which are unordered , mutable and can't allows duplicates

set1 = {1,2,3,1,2,4,5}
print(type(set1))
print(set1) #doesn't allows duplicates

for x in set1:
    print(x)

set2 = set()

set2.add(1)
print(set2)

set1.remove(2) , print(set1) 
set1.discard(1) , print(set1)


#UNION AND INTERSECTION 
odd = {1,3,5,7,9}
even = {2,4,6,8,10}
primes = {1,3,5,7,11}

print(odd.union(even)) #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(odd.intersection(primes)) #{1, 3, 5, 7}

