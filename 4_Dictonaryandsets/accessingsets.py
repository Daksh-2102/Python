'''We generally can't access items/elements of set through indexing, but we can access the 
elements through looping
'''
#for loop

set1 = {
    1,2,3,'vasu','daksh',4
}
print("Elements of set are : ")
for i in set1:
    print(i)
    

#To check whether that element is present or not in the set

if input("Enter set1 element ") in set1:
    print("yes present sir")
else:
    print("absent sir")