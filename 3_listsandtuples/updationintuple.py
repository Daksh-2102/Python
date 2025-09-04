''' Since we know that tuples are immutable, so we directly can't perform modifications in tuples.
To do modifications in tuple, firstly we have to convert tuple into list,perform changes and then
convertback them into tuple
'''

tuple1 = (2,3,4)

list1 = list(tuple1) # conversion of tuple into list

list1[0] = 1 #modifications takes place in list
tuple1 = tuple(list1)

print(tuple1) #(1, 3, 4)

#2. add using append

x = ('app','map')

y = list(x)

y.append("rat")

x = tuple(y)
print(x) #('app', 'map', 'rat')

#3 add two tuple

t1 = (1,2,3)
t2 = (4,5)

t3 = t1+t2
print(t3) #(1, 2, 3, 4, 5)