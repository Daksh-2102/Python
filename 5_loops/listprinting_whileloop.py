#printing the list using the whle loop.
#[1,4,9,16,25,26,49,64,81,100]

list1 = [1,4,9,16,25,26,49,64,81,100]

print("list elements :",end =" ")
i = 1
while i<=10:
    print(i*i,end=" ")
    i+=1
print('\n\n')
#2.using index values

list2 = ['vasu','daksh','abd','virat','rohit','ansh']

i = 0 #index starts from 0
while i < len(list2):
    print(list2[i])
    i+=1
