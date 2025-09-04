#methods of concetanating various lists

#1. + :- just add list1 + list 2

#2. using append func

list1 = [1,2,3]
list2 = [4,5,6]

print("both lists after joining :")
for x in list2:
    list1.append(x)

print(list1) #[1, 2, 3, 4, 5, 6]

#3 using extend func
list3 = ['a','b','c']
list4 = ['d','e','f']

list3.extend(list4)
print(list3)
