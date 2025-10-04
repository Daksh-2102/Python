'''Lists are mutable data types in py i.e it can stores duplicates as well 
Denoted by [] '''

mylist = [1,'app','rat',69]

print(mylist)

#create empty list
mylist1 = list()
print(mylist1)


for i in mylist:
    print(i)

#Add items 
mylist1.append('bat')
print(mylist1)

#check presence 

if 1 in mylist: #yes
    print("yes")
else:
    print("no")
    
#inserting at particular index : use insert method

mylist1.insert(0,'mouse')
print(mylist1)
