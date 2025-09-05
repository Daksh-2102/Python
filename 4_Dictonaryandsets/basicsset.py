#basics of set
#Set is a collection of immutable items that cannot be modified and can store only unique items.

#We can store all the datatypes and tuple in the set but we cannot store lists and dict in it as they are mutable.

set1 = {
    1,'rat',2,9.99,'kaka'
}

print(set1)
print(type(set1))

#Sets are ordered pairs and duplicacy is removed

set2 = { 1,2,2,2,'ratuu','catuu',89.99,3}
print(set2)
print(len(set2))