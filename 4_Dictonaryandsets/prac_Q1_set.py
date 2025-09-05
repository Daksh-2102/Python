#add 9 and 9.0 as seprate values in the set. 

set1 = { 
    9,'9.0'
}
print(type(set1))

print(set1)

#2 way to solve this

set2 = { 
    ('int',9),('float',9.0)
}
print(set2)
print(type(set2     ))