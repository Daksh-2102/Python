#We can add set items using different functions.

set1 = { 1,2,3,4}
#1. .add() :- It can add elements to the list
set1.add(4)
print(set1)

#2. .update() :- used to add one set to the another set
set2 = {5,5,6}
set1.update(set2)
print(set1)

#3. we can add lists/tuples to the set using .update() func.
list1 = [10,9]
set1.update(list1)
print(set1)