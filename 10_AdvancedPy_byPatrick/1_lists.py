'''Lists are mutable i.e can be modified  data types in py and it can stores duplicates as well 
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

print(mylist[-4: ]) #accesing items using neg indexing 

mylist[0] = "2" #changing items
print(mylist)

#we can add items using append , insert and extend which helps to add another list

#reversing list cool way
mylist3 = [1,2,3,4,5]

print(mylist3[::-1]) #prints the above list in reverse order

print(mylist3[::1]) #prints the whole list