#lists methods
list = [4,1,9,2]
print(list)
#1. list.append(number) :- It adds any element in the end of the list.
list.append(11) #[4,1,9,2,11]
print(list)

#2. list.sort() :- it sorts the elements in ascending order.
list.sort() #[1,2,4,9,11]
print(list)

#3. list.sort(reverse=True) :- It sorts the elements in descending order.
list.sort(reverse=True)
print(list) # [11,9,4,2,1]

#4. list.reverse :- It reverses the elements of the list.
list.reverse()
print(list) # It revrses the previous list i.e [1,2,4,9,11]

#5. list.insert(index,element)
list.insert(0,123)
list.insert(4,13)
print(list)