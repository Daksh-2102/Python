## Collections ->> namedtuple
from collections import namedtuple

#namedtuple is used to create tuple in a modified way

Point = namedtuple('Point','x,y')

pt = Point(1,-8)

print(pt) #Point(x=1, y=-8)
print(pt.x , pt.y)

###example 2

# Create a named tuple type called 'Person'
Person = namedtuple('Person', ['name', 'age', 'city'])

# Create an object (like a record)
p1 = Person('Daksh', 21, 'Delhi')

print(p1)
print(p1.name,p1.age,p1.city) 
