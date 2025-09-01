#Slicing in lists
#It returns complete str or int and its indexing is from 0 to n-1

list = [10,"Daksh",88,"vasu"]

print(list[0:1]) #returns 10 only
print(list[0:]) #return the complete list as it consider the blank space as len(list) 
print(list[:3]) #return the values from index 0 as it considers the blank space as list[0]
print(list[0:len(list)]) #returns the complete list 
print(list[0:4]) #for getting the complete list, we have to run the list from 0 to n-1 index