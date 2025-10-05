'''Tuple is immutable datatype that can store duplicate items ''' 

mytup = (1,'2',3,'rat')

print(type(mytup))
print(mytup)

tup1 = (1) #this is consider as int type
tup2 = (1,) #this is now consider as tuple 
print(type(tup1))

print(mytup[3])

# mytup[0] = 10 # tuples doesnot allows item modification
print(mytup)
#to do so convert it into list make changes and then convert back into tuple.

for i in range(len(mytup)):
    print(mytup[i])