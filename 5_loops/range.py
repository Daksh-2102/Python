'''range function :-Range function returns a sequence of numbers starting from 0 by default
and increment by 1 and stops at particular no. '''
#there r 3 ways of writing range
#1.range(n)

for i in range(5):
    print(i,end =" ")
print("\nend\n")

#2. range(start,end)
for el in range(1,6):
    print(el,end = " ")
print("\nend\n")

#3. range(start,end,step)
for x in range(1,10,2):
    print(x,end = " ")