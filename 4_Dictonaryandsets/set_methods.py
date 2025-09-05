#Methods of sets

set1 = {1,2,'daksh','vasu',7}

#1. set.add() :- Add elements into the set
set1.add("raghu")
set1.add(4)
print(set1)
print(type(set1))
 
#2. set.remove :- removes elements from the set
set1.remove("raghu")
print(set1)

#3. .clear() :- clears all the elements of the set and shows the length of set = 0
#set1.clear()
print(set1) # it will print the empty set i.e set()
print(len(set1)) #0

#4. .pop() :- pops out the random value
set1.pop()
print(set1)
