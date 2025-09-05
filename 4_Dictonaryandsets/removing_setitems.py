#removing set elements.

#1. .remove() :- removes particular element from the set
set1 = {1,2,3,4}
(set1.remove(3))
print(set1)

#2.pop() :- will remove random item from the set
set1.pop()
print(set1)

#3. .clear and del keyword will clear the set 
set1.clear()
print(len(set1)) #0
print(set1) #it will print empty set i.e set()