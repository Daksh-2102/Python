#Join :- is the methods of combining two or more sets in the single set.

#1. union/update() or | :- used to combine two or more sets in sinle set.
set1 = {1,2,3}
set2 = {2,3,4,5}
print("Union of two sets are  :")
print(set1 | set2)

#2.intersection or & :- used to print the duplicates of the two or more sets.
print("intersetion of two sets are :")
set3 = set1.intersection(set2)
print(set3) #2, 3}

'''intersetion_update :- will work same as .intersetion but it will update the original set 
rather than working on different set '''

#3. Difference or A - B :- returns the newset containing only elements that r only in set1 not in set2
set4 = {10,20,30}
set5 = {30,40,50}
print(set4 - set5) #{10, 20}

set4.intersection_update(set5)  
print(set4) #{30}
print(set5) #{40, 50, 30}

#4. symmetric difference  :- keeps all the elements except the duplicates

print(set1 ^ set2)

#symmetric_difference_update :- will perform the same thing but in the original set rather than making a newset
