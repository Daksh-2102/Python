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