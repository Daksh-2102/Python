#UNPACKING THE TUPLES

tuple = ('vasu','daksh','raghu')
(a,b,c) = tuple
print(a)
print(b)
print(c)

#if the tuple is big we can assign a single var to soo many tuple elements
tup = ('app','rAT','bat','mat','hat','saT')

(m,n,*o) = tup

print(m,n,o) #app rAT ['bat', 'mat', 'hat', 'saT']